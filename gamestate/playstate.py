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

    def handle_events(self, events):
        for event in events:
            command = None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    command = "REMOVE"
                elif event.key == pygame.K_RETURN:
                    command = "ENTER"
                elif event.unicode.isalpha():
                    command = event.unicode.upper()

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
                self.board.delete_letter()
                self.users_word.pop()
        elif command == "ENTER":
            if len(self.users_word) == 5:
                self.board.check_tiles(self.users_word, self.word_to_guess)
                self.keyboard.change_color(self.board.rows[self.board.current_row].tiles)

                is_win = "".join(self.users_word) == self.word_to_guess.strip()
                is_lose = self.board.current_row == 5

                if is_win or is_lose:
                    new_state = SummaryState(self.game)
                    new_state.word_to_guess = self.word_to_guess
                    new_state.used_rows = self.board.current_row + 1
                    new_state.won = is_win
                    return new_state

                self.board.next_row()
                self.users_word = []
            return None
        elif len(command) == 1:
            if len(self.users_word) < 5:
                self.board.change_letter(command)
                self.users_word.append(command)

    def draw(self, surface):
        surface.fill(settings.get_window_color())
        self.keyboard.create_keyboard(surface)
        self.board.create_board(surface)