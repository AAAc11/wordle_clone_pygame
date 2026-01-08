import pygame
from settings import font, GRAY, YELLOW, GREEN, WHITE


class Tile:
    def __init__(self, x, y):
        self.letter = ''
        self.x = x
        self.y = y
        self.rect = 0
        self.status = 'unguessed'
        self.color = GRAY
        self.scale = 1.0

    def create_tile(self, window):
        thickness = 2
        self.rect = pygame.Rect(self.x, self.y, 50 * self.scale, 50 * self.scale)
        if self.letter != "":
            thickness = 4
            pygame.draw.rect(window, self.color, self.rect, thickness)
            text_surface = font.render(self.letter, True, WHITE)
            text_rect = text_surface.get_rect(center=self.rect.center)
            window.blit(text_surface, text_rect)
        else:
            pygame.draw.rect(window, self.color, self.rect, thickness)

    def change_status(self, new_status):
        self.status = new_status
        if new_status == 'exists':
            self.color = YELLOW
        elif new_status == 'guessed':
            self.color = GREEN


    def change_letter(self, letter):
        if len(letter) == 1:
            self.letter = letter

    def animation(self):
        pass