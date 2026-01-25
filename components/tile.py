import pygame
from settings import *
import settings


class Tile:
    def __init__(self, x, y):
        self.letter = ''
        self.x = x
        self.y = y
        self.rect = 0
        self.status = 'unguessed'
        self.color = LIGHT_GRAY
        self.shake_scale = 0
        self.is_shaking = False
        self.shake_movements = []

    def start_shake(self):
        self.shake_movements = [-7, 7, -7, 7, -5, 5, -5, 5, -2, 2, -2, 2, 0]
        self.is_shaking = True

    def shake_animation(self):
        if self.is_shaking:
            if len(self.shake_movements) > 0:
                self.shake_scale = self.shake_movements.pop(0)
            else:
                self.is_shaking = False
                self.shake_scale = 0


    def create_tile(self, window):
        self.shake_animation()

        thickness = 2
        current_border_color = self.color
        if self.color == LIGHT_GRAY:
            if not settings.IS_DARK_MODE:
                current_border_color = (180, 180, 180)
        else:
            thickness = 0

        x = self.x + self.shake_scale
        self.rect = pygame.Rect(x, self.y, 50, 50)

        pygame.draw.rect(window, current_border_color, self.rect, thickness)

        if thickness == 0:
            font_color = WHITE
        else:
            font_color = WHITE if settings.IS_DARK_MODE else BLACK

        text_surface = small_font.render(self.letter, True, font_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        window.blit(text_surface, text_rect)


    def change_color(self, new_color):
        self.color = new_color

    def change_letter(self, letter):
        if len(letter) == 1:
            self.letter = letter

    def delete_letter(self):
        self.letter = ""

    def get_letter(self):
        return self.letter
