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

running = True
while running:
    window.fill(WINDOW_COLOR)
    window.blit(text, [165, 30])

    x = 130
    y = 100
    for i in range(5):
        for j in range(5):
            RECT_PARAMETERS = pygame.Rect(x, y, 50, 50)
            pygame.draw.rect(window, WHITE, RECT_PARAMETERS, 2)
            x += 60
        x = 130
        y += 60


    keyboard_display(window)
    pygame.display.flip()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
