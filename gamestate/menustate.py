from gamestate.state import State
from gamestate.playstate import PlayState
import settings
from settings import *


class MenuState(State):
    def __init__(self, game):
        super().__init__(game)
        self.button_play = pygame.Rect(WORDLE_SCREEN_WIDTH // 2 - 150, 450, 140, 60)
        self.button_ai = pygame.Rect(WORDLE_SCREEN_WIDTH // 2 + 10, 450, 140, 60)

        self.difficulty_rect = pygame.Rect(20, WORDLE_SCREEN_HEIGHT - 60, 130, 40)

        #przełacznik jasny/ciemny tryb
        self.switch_w, self.switch_h = 40, 20
        self.switch_rect = pygame.Rect(WORDLE_SCREEN_WIDTH - 60, WORDLE_SCREEN_HEIGHT - 40, self.switch_w,
                                       self.switch_h)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.difficulty_rect.collidepoint(event.pos):
                    settings.IS_HARD_MODE = not settings.IS_HARD_MODE

                if self.switch_rect.collidepoint(event.pos):
                    settings.IS_DARK_MODE = not settings.IS_DARK_MODE

                if self.button_play.collidepoint(event.pos):
                    return PlayState(self.game)

                if self.button_ai.collidepoint(event.pos):
                    print("AI Player mode coming soon...")
        return self

    def toggle_mode(self):
        settings.IS_DARK_MODE = not settings.IS_DARK_MODE

    def draw_static_logo(self, surface):
        word = "WORDLE"
        tile_size = 65
        spacing = 12
        total_width = len(word) * (tile_size + spacing) - spacing
        start_x = (WORDLE_SCREEN_WIDTH - total_width) // 2
        start_y = 150

        for i, char in enumerate(word):
            rect = pygame.Rect(start_x + i * (tile_size + spacing), start_y, tile_size, tile_size)
            pygame.draw.rect(surface, GREEN, rect)

            char_surf = medium_font.render(char, True, WHITE)
            char_rect = char_surf.get_rect(center=rect.center)
            surface.blit(char_surf, char_rect)

    def draw(self, surface):
        surface.fill(settings.get_window_color())

        self.draw_static_logo(surface)

        ui_color = WHITE if settings.IS_DARK_MODE else BLACK

        #przycisk play
        pygame.draw.rect(surface, DARK_GRAY, self.button_play, border_radius=10)
        pygame.draw.rect(surface, ui_color, self.button_play, width=3, border_radius=10)
        play_txt = small_font.render("PLAY", True, WHITE)
        surface.blit(play_txt, play_txt.get_rect(center=self.button_play.center))

        #przycisk ai player
        pygame.draw.rect(surface, DARK_GRAY, self.button_ai, border_radius=10)
        pygame.draw.rect(surface, ui_color, self.button_ai, width=3, border_radius=10)
        ai_txt = very_small_font.render("AI PLAYER", True, WHITE)
        surface.blit(ai_txt, ai_txt.get_rect(center=self.button_ai.center))

        #przycisk z trudnością gry (easy/hard)
        diff_color = RED if settings.IS_HARD_MODE else GREEN
        pygame.draw.rect(surface, diff_color, self.difficulty_rect, border_radius=8)

        diff_text = "HARD" if settings.IS_HARD_MODE else "EASY"

        diff_surf = very_small_font.render(f"MODE: {diff_text}", True, WHITE)
        surface.blit(diff_surf, diff_surf.get_rect(center=self.difficulty_rect.center))

        #przełącznik dark mode
        bg_color = (100, 100, 100)
        pygame.draw.rect(surface, bg_color, self.switch_rect, border_radius=self.switch_h // 2)

        circle_radius = (self.switch_h // 2) - 2
        if settings.IS_DARK_MODE:
            circle_x = self.switch_rect.left + self.switch_h // 2
        else:
            circle_x = self.switch_rect.right - self.switch_h // 2
        pygame.draw.circle(surface, WHITE, (circle_x, self.switch_rect.centery), circle_radius)

        mode_label = very_small_font.render("THEME", True, ui_color)
        surface.blit(mode_label, (self.switch_rect.left - 55, self.switch_rect.centery - 7))