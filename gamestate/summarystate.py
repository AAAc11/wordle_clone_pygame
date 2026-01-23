import sys
from gamestate.state import State
from settings import *
import settings


class SummaryState(State):
    def __init__(self, game):
        super().__init__(game)
        self.word_to_guess = ""
        self.won = False
        self.used_rows = 0
        self.button_exit = pygame.Rect(WORDLE_SCREEN_WIDTH // 2 - 110, 450, 100, 50)
        self.button_save = pygame.Rect(WORDLE_SCREEN_WIDTH // 2 + 10, 450, 100, 50)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.button_exit.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                elif self.button_save.collidepoint(event.pos):
                    self.save_game_to_file()

    def save_game_to_file(self):
        print("Saving game to file...")

    def draw(self, surface):
        surface.fill(settings.get_window_color())

        main_text_color = WHITE if settings.IS_DARK_MODE else BLACK

        status_text = "YOU WON!" if self.won else "YOU LOST!"
        status_color = GREEN if self.won else RED
        status_surf = small_font.render(status_text, True, status_color)
        status_rect = status_surf.get_rect(center=(WORDLE_SCREEN_WIDTH // 2, 150))
        surface.blit(status_surf, status_rect)

        answer_text = small_font.render(f"The answer was: {self.word_to_guess.upper()}", True, main_text_color)
        ans_rect = answer_text.get_rect(center=(WORDLE_SCREEN_WIDTH // 2, 250))
        surface.blit(answer_text, ans_rect)

        btn_color = DARK_GRAY if settings.IS_DARK_MODE else (180, 180, 180)
        btn_text_color = WHITE if settings.IS_DARK_MODE else BLACK
        btn_border_color = WHITE if settings.IS_DARK_MODE else DARK_GRAY

        pygame.draw.rect(surface, btn_color, self.button_exit, border_radius=6)
        pygame.draw.rect(surface, btn_border_color, self.button_exit, width=2, border_radius=6)
        exit_surf = small_font.render("EXIT", True, btn_text_color)
        surface.blit(exit_surf, exit_surf.get_rect(center=self.button_exit.center))

        pygame.draw.rect(surface, btn_color, self.button_save, border_radius=6)
        pygame.draw.rect(surface, btn_border_color, self.button_save, width=2, border_radius=6)
        save_surf = small_font.render("SAVE", True, btn_text_color)
        surface.blit(save_surf, save_surf.get_rect(center=self.button_save.center))