import pygame
pygame.font.init()
pygame.init()

DARK_MODE_BG = (31, 27, 27)
LIGHT_MODE_BG = (230, 230, 230)

IS_DARK_MODE = True

def get_window_color():
    return DARK_MODE_BG if IS_DARK_MODE else LIGHT_MODE_BG

IS_HARD_MODE = False

WHITE = (255, 255, 255)
GREEN = (79, 235, 52)
YELLOW = (235, 214, 52)
RED = (252, 3, 3)
DARK_GRAY = (74, 74, 73)
LIGHT_GRAY = (166, 166, 166)
BLACK = (0, 0, 0)
WORDLE_SCREEN_WIDTH = 550
WORDLE_SCREEN_HEIGHT = 700

very_small_font = pygame.font.SysFont(None, 21)
small_font = pygame.font.SysFont(None, 50)
medium_font = pygame.font.SysFont(None, 70)