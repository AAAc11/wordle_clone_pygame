import pygame

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700
FPS = 30
WINDOW_COLOR = (31, 27, 27)
FRAME_COLOR = (235, 235, 235)
GAP = 20


pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
window.fill(WINDOW_COLOR)
pygame.display.update()

x = 110
y = 100
for i in range(0,5):
    for j in range(0, 5):
        RECT_PARAMETERS = pygame.Rect(x, y, 50, 50)
        pygame.draw.rect(window, FRAME_COLOR, RECT_PARAMETERS, 2)
        x += 60
        j += 1
    x = 110
    y += 60
    i += 1

pygame.draw.rect(window, FRAME_COLOR, (40, 450, 40, 55), 0, border_radius=3)

pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
