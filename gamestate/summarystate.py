import sys
import random
from gamestate.state import State
from datetime import datetime
from settings import *
import settings


class SummaryState(State):
    def __init__(self, game):
        super().__init__(game)
        self.word_to_guess = ""
        self.won = False
        self.is_ai = False
        self.show_saved_msg = False
        self.confetti_particles = []

        #inicjalizowanie dźwięku
        pygame.mixer.init()
        self.sound_played = False
        try:
            self.victory_sound = pygame.mixer.Sound("other/victory.mp3")
            self.defeat_sound = pygame.mixer.Sound("other/defeat.mp3")
        except pygame.error:
            print("Error: Cannot load the sound")
            self.victory_sound = None
            self.defeat_sound = None

        self.button_exit = pygame.Rect(WORDLE_SCREEN_WIDTH // 2 - 150, 450, 140, 60)
        self.button_save = pygame.Rect(WORDLE_SCREEN_WIDTH // 2 + 10, 450, 140, 60)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.button_exit.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                elif self.button_save.collidepoint(event.pos):
                    self.save_game_to_file()
        return self

    def save_game_to_file(self):
        #zapis wyniku gry do pliku
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        result = "VICTORY" if self.won else "DEFEAT"
        log_entry = f"[{now}] Result: {result}, Word to guess: {self.word_to_guess.upper()}\n"

        try:
            with open("wyniki.txt", "a", encoding="utf-8") as file:
                file.write(log_entry)
                self.show_saved_msg = True
        except Exception as e:
            print(f"Error: {e}")

    def _create_confetti(self):
        for _ in range(100):
            self.confetti_particles.append({
                "x": random.randint(0, WORDLE_SCREEN_WIDTH),
                "y": random.randint(-WORDLE_SCREEN_HEIGHT, 0),
                "size": random.randint(5, 10),
                "color": random.choice([GREEN, YELLOW, WHITE, RED, (52, 152, 219)]),
                "speed": random.uniform(2, 5)
            })

    def draw(self, surface):
        #w zależności od wyniku dźwięk i konfetti
        if not self.sound_played:
            if self.won:
                if self.victory_sound:
                    self.victory_sound.play()
                self._create_confetti()
            else:
                if self.defeat_sound:
                    self.defeat_sound.play()
            self.sound_played = True

        surface.fill(settings.get_window_color())

        #rysowanie konfetti
        if self.won:
            for p in self.confetti_particles:
                pygame.draw.rect(surface, p["color"], (p["x"], p["y"], p["size"], p["size"]))
                p["y"] += p["speed"]
                p["x"] += random.uniform(-1, 1)
                if p["y"] > WORDLE_SCREEN_HEIGHT:
                    p["y"] = random.randint(-50, -10)
                    p["x"] = random.randint(0, WORDLE_SCREEN_WIDTH)

        #motyw
        ui_color = WHITE if settings.IS_DARK_MODE else BLACK

        #kolor wyniku
        status_color = GREEN if self.won else RED

        #wynik gry
        main_result = "VICTORY" if self.won else "DEFEAT"
        prefix = "AI PLAYER " if self.is_ai else ""
        full_status_text = f"{prefix}{main_result}"
        font_to_use = small_font if self.is_ai else medium_font

        status_surf = font_to_use.render(full_status_text, True, status_color)
        status_rect = status_surf.get_rect(center=(WORDLE_SCREEN_WIDTH // 2, 150))
        surface.blit(status_surf, status_rect)

        #wyświetlenie odpowiedzi
        label_surf = very_small_font.render("THE ANSWER WAS:", True, ui_color)
        surface.blit(label_surf, label_surf.get_rect(center=(WORDLE_SCREEN_WIDTH // 2, 240)))

        answer_surf = small_font.render(self.word_to_guess.upper(), True, ui_color)
        surface.blit(answer_surf, answer_surf.get_rect(center=(WORDLE_SCREEN_WIDTH // 2, 285)))

        #przycisk exit i save
        btn_color = DARK_GRAY
        for btn, txt in [(self.button_exit, "EXIT"), (self.button_save, "SAVE")]:
            pygame.draw.rect(surface, btn_color, btn, border_radius=10)
            pygame.draw.rect(surface, ui_color, btn, width=3, border_radius=10)
            t_surf = small_font.render(txt, True, WHITE)
            surface.blit(t_surf, t_surf.get_rect(center=btn.center))

        #wiadomość, że gra została zapisana
        if self.show_saved_msg:
            saved_txt = very_small_font.render("GAME PROGRESS SAVED", True, GREEN)
            surface.blit(saved_txt, saved_txt.get_rect(center=(WORDLE_SCREEN_WIDTH // 2, 550)))