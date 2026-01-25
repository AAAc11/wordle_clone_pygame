import pygame
from gamestate.state import State
from gamestate.summarystate import SummaryState
from components import Board, Keyboard
from library import word_draw
import settings


class PlayState(State):
    def __init__(self, game):
        super().__init__(game)
        self.board = Board()
        self.keyboard = Keyboard()
        self.word_to_guess, self.list_of_words = word_draw()
        self.users_word = []
        print(f"Word to guess: {self.word_to_guess}")

        pygame.mixer.init()
        try:
            self.click_sound = pygame.mixer.Sound("other/click.wav")
            self.click_sound.set_volume(0.5)
        except pygame.error:
            print("Warning: Could not load other/click.wav")
            self.click_sound = None

        try:
            with open("library/przefiltrowany_slownik.txt", "r", encoding="utf-8") as f:
                self.valid_words = {line.strip().upper() for line in f}
        except FileNotFoundError:
            print("Error: No dictionary found")
            self.valid_words = set()

    def handle_events(self, events):
        for event in events:
            command = None

            #klawiatura fizyczna
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    command = "REMOVE"
                elif event.key == pygame.K_RETURN:
                    command = "ENTER"
                elif event.unicode.isalpha():
                    command = event.unicode.upper()

            #klawiatura ekranowa
            elif event.type == pygame.MOUSEBUTTONDOWN:
                command = self.keyboard.which_letter_is_clicked(event.pos)

            if command:
                result = self._process_command(command)
                if result is not None:
                    return result

        return self

    def _process_command(self, command):
        if command == "REMOVE":
            if len(self.users_word) > 0:
                if self.click_sound:
                    self.click_sound.play()
                self.board.delete_letter()
                self.users_word.pop()

        elif command == "ENTER":
            if len(self.users_word) == 5:
                current_attempt = "".join(self.users_word).upper()

                #sprwdzenie czy słowo istnieje
                if current_attempt not in self.valid_words:
                    self.board.shake_animation()
                    return None

                if settings.IS_HARD_MODE and self.board.current_row > 0:
                    last_row = self.board.rows[self.board.current_row - 1]

                    for i, tile in enumerate(last_row.tiles):
                        #zielona litera na tym samym miejscu
                        if tile.color == settings.GREEN:
                            if current_attempt[i] != tile.letter:
                                print(f"Hard Mode: {tile.letter} must be at position {i + 1}")
                                self.board.shake_animation()
                                return None

                        #żółta litera musi być użyta
                        elif tile.color == settings.YELLOW:
                            if tile.letter not in current_attempt:
                                print(f"Hard Mode: Must use letter {tile.letter}")
                                self.board.shake_animation()
                                return None

                self.board.check_tiles(self.users_word, self.word_to_guess)

                #obsługa kolorów na klawiaturze
                current_tiles = self.board.rows[self.board.current_row].tiles
                self.keyboard.change_color(current_tiles)

                #sprawdzenie wygranej lub przegranej
                is_win = current_attempt == self.word_to_guess.strip().upper()
                is_lose = self.board.current_row == 5

                if is_win or is_lose:
                    from gamestate import SummaryState
                    new_state = SummaryState(self.game)
                    new_state.word_to_guess = self.word_to_guess
                    new_state.used_rows = self.board.current_row + 1
                    new_state.won = is_win
                    return new_state

                self.board.next_row()
                self.users_word = []

        elif len(command) == 1 and command.isalpha():
            #obsługa wpisywanych liter
            if len(self.users_word) < 5:
                if self.click_sound:
                    self.click_sound.play()
                self.board.change_letter(command)
                self.users_word.append(command.upper())

        return None

    def draw(self, surface):
        surface.fill(settings.get_window_color())
        self.keyboard.create_keyboard(surface)
        self.board.create_board(surface)