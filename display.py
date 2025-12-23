import pygame

from keyboard import keyboard_display

SCREEN_WIDTH = 550
SCREEN_HEIGHT = 700
WINDOW_COLOR = (31, 27, 27)
WHITE = (255, 255, 255)


pygame.init()
pygame.font.init()
font = pygame.font.SysFont(None, 70)
text = font.render('WORDLE', True, WHITE)
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
window.fill(WINDOW_COLOR)
pygame.display.set_caption("WORDLE")
window.blit(text, [165, 30])
pygame.display.update()

x = 130
y = 100
for i in range(0,5):
    for j in range(0, 5):
        RECT_PARAMETERS = pygame.Rect(x, y, 50, 50)
        pygame.draw.rect(window, WHITE, RECT_PARAMETERS, 2)
        x += 60
        j += 1
    x = 130
    y += 60
    i += 1

    keyboard_display(window, WHITE)

pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
