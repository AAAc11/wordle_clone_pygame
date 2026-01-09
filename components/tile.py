import pygame
from settings import small_font, LIGHT_GRAY, YELLOW, GREEN, WHITE


class Tile:
    def __init__(self, x, y):
        self.letter = ''
        self.x = x
        self.y = y
        self.rect = 0
        self.status = 'unguessed'
        self.color = LIGHT_GRAY
        self.scale = 1.0

    def create_tile(self, window):
        thickness = 2
        if self.color != LIGHT_GRAY:
            thickness = 0
        self.rect = pygame.Rect(self.x, self.y, 50 * self.scale, 50 * self.scale)
        pygame.draw.rect(window, self.color, self.rect, thickness)
        text_surface = small_font.render(self.letter, True, WHITE)
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

    def animation(self):
        pass