import pygame
pygame.font.init()
pygame.init()

WINDOW_COLOR = (31, 27, 27)
WHITE = (255, 255, 255)
GREEN = (79, 235, 52)
YELLOW = (235, 214, 52)
DARK_GRAY = (74, 74, 73)
LIGHT_GRAY = (166, 166, 166)
BLACK = (0, 0, 0)
WORDLE_SCREEN_WIDTH = 550
WORDLE_SCREEN_HEIGHT = 700

very_small_font = pygame.font.SysFont(None, 21)
small_font = pygame.font.SysFont(None, 50)
medium_font = pygame.font.SysFont(None, 70)