import pygame

pygame.font.init()

WHITE = (255, 255, 255)
WINDOW_COLOR = (31, 27, 27)

def empty_frames(window):
    x = 130
    y = 100
    for i in range(5):
        for j in range(5):
            rect_parameters = pygame.Rect(x, y, 50, 50)
            pygame.draw.rect(window, WHITE, rect_parameters, 2)
            x += 60
        x = 130
        y += 60

class LetterArea:
    def __init__(self, window, x, y):
        self.window = window
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
        self.letter = ""
        self.color = None
        self.font = pygame.font.Font(None, 50)

    def letter_display(self, window):
        if self.color:
            pygame.draw.rect(window, self.color, self.rect)

        thickness = 2
        if self.letter != "":
            thickness = 4
            pygame.draw.rect(window, (100, 100, 100), self.rect, thickness)
        else:
            pygame.draw.rect(window, (200, 200, 200), self.rect, thickness)

        if self.letter != "":
            text_surface = self.font.render(self.letter, True, WHITE)
            text_rect = text_surface.get_rect(center=self.rect.center)
            window.blit(text_surface, text_rect)


    def set_letter(self, letter):
        self.letter = letter

    def set_color(self, color):
        self.color = color