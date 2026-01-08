import pygame
from components.board import Board

pygame.init()
pygame.font.init()

running = True

WORDLE_SCREEN_WIDTH = 550
WORDLE_SCREEN_HEIGHT = 700
WINDOW_COLOR = (31, 27, 27)


main_window = pygame.display.set_mode((WORDLE_SCREEN_WIDTH, WORDLE_SCREEN_HEIGHT))
main_window.fill(WINDOW_COLOR)
pygame.display.set_caption("WORDLE")


board = Board()

while running:
    main_window.fill(WINDOW_COLOR)

    board.create_board(main_window)

    pygame.display.flip()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
