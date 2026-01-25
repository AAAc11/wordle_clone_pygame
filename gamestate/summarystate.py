import sys
import pygame
from gamestate.state import State
from settings import *
import settings


class SummaryState(State):
    def __init__(self, game):
        super().__init__(game)
        self.word_to_guess = ""
        self.won = False
        self.used_rows = 0

        self.button_exit = pygame.Rect(WORDLE_SCREEN_WIDTH // 2 - 150, 450, 140, 60)
        self.button_save = pygame.Rect(WORDLE_SCREEN_WIDTH // 2 + 10, 450, 140, 60)

        pygame.mixer.init()
        self.sound_played = False
        try:
            self.victory_sound = pygame.mixer.Sound("other/victory.mp3")
            self.defeat_sound = pygame.mixer.Sound("other/defeat.mp3")
        except pygame.error:
            print("Error: Cannot load the sound")
            self.victory_sound = None
            self.defeat_sound = None

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
        print("Saving game to file...")

    def draw(self, surface):
        if not self.sound_played:
            if self.won and self.victory_sound:
                self.victory_sound.play()
            elif not self.won and self.defeat_sound:
                self.defeat_sound.play()
            self.sound_played = True

        surface.fill(settings.get_window_color())

        ui_color = WHITE if settings.IS_DARK_MODE else BLACK

        status_text = "YOU WON!" if self.won else "YOU LOST!"
        status_color = GREEN if self.won else RED


        status_surf = medium_font.render(status_text, True, status_color)
        status_rect = status_surf.get_rect(center=(WORDLE_SCREEN_WIDTH // 2, 150))
        surface.blit(status_surf, status_rect)

        label_surf = very_small_font.render("THE ANSWER WAS:", True, ui_color)
        label_rect = label_surf.get_rect(center=(WORDLE_SCREEN_WIDTH // 2, 240))
        surface.blit(label_surf, label_rect)


        answer_surf = small_font.render(self.word_to_guess.upper(), True, ui_color)
        answer_rect = answer_surf.get_rect(center=(WORDLE_SCREEN_WIDTH // 2, 285))
        surface.blit(answer_surf, answer_rect)

        btn_color = DARK_GRAY
        btn_border_color = ui_color

        #przycisk exit
        pygame.draw.rect(surface, btn_color, self.button_exit, border_radius=10)
        pygame.draw.rect(surface, btn_border_color, self.button_exit, width=3, border_radius=10)
        exit_surf = small_font.render("EXIT", True, WHITE)
        surface.blit(exit_surf, exit_surf.get_rect(center=self.button_exit.center))

        #przycisk save
        pygame.draw.rect(surface, btn_color, self.button_save, border_radius=10)
        pygame.draw.rect(surface, btn_border_color, self.button_save, width=3, border_radius=10)
        save_surf = small_font.render("SAVE", True, WHITE)
        surface.blit(save_surf, save_surf.get_rect(center=self.button_save.center))