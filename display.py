
import pygame

from keyboard import keyboard_display, buttons
from rows import LetterArea


SCREEN_WIDTH = 550
SCREEN_HEIGHT = 700
WINDOW_COLOR = (31, 27, 27)
WHITE = (255, 255, 255)

grid = []
current_row = 0
current_col = 0
start_x = 130
start_y = 90


pygame.init()
pygame.font.init()
font = pygame.font.SysFont(None, 70)
text = font.render('WORDLE', True, WHITE)
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
window.fill(WINDOW_COLOR)
pygame.display.set_caption("WORDLE")

keyboard_display(window)

for row in range(6):
    row_tiles = []
    for col in range(5):
        x = start_x + (col * 60)
        y = start_y + (row * 60)
        new_tile = LetterArea(window, x, y)
        row_tiles.append(new_tile)
    grid.append(row_tiles)

running = True
while running:
    window.fill(WINDOW_COLOR)
    window.blit(text, [165, 30])

    for button in buttons.values():
        button.creating_area()

    for row in grid:
        for tile in row:
            tile.letter_display(window)

    pygame.display.flip()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos

            for button in buttons.values():
                if button.rect.collidepoint(mouse_position):
                    clicked_letter = button.letter
                    if clicked_letter == "ENTER" and current_col == 5:
                        current_row += 1
                        current_col = 0
                        print("klkik eneter")
                    elif clicked_letter == "RETURN":
                        if current_col > 0:
                            current_col -= 1
                            grid[current_row][current_col].set_letter("")
                        print("klik return")

                    else:
                        if current_col < 5:
                            grid[current_row][current_col].set_letter(clicked_letter)
                            current_col += 1

pygame.quit()
