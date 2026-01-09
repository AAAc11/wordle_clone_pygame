from settings import WHITE, BLACK
import pygame


class Key:
    def __init__(self, letter, x, y, width, font):
        self.letter = letter
        self.color = WHITE
        self.x = x
        self.y = y
        self.width = width
        self.rect = pygame.Rect(self.x, self.y, width , 55)
        self.font = font

    def change_color(self, color):
        self.color = color

    def create_key(self, window):
        surface = pygame.draw.rect(window, self.color, self.rect, 0,
                                   border_radius=3)
        letter_surface = self.font.render(self.letter, True, BLACK)
        letter_rect = letter_surface.get_rect(center=surface.center)
        window.blit(letter_surface, letter_rect)

    def is_clicked(self, mouse_position):
        if self.rect.collidepoint(mouse_position):
            return self.letter
        return None


