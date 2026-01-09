import pygame
from components.board import Board
from components.keyboard import Keyboard
from word_of_the_day import word_draw

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
keyboard = Keyboard()
clicked_letter = None
users_word = []
word_to_guess = word_draw()

print(word_to_guess)

while running:
    main_window.fill(WINDOW_COLOR)

    keyboard.create_keyboard(main_window)
    board.create_board(main_window)

    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        command = None

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                command = "REMOVE"
            elif event.key == pygame.K_RETURN:
                command = "ENTER"
            elif event.unicode.isalpha():
                command = event.unicode.upper()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            command = keyboard.which_letter_is_clicked(event.pos)

        if command:
            if command == "REMOVE":
                if len(users_word) > 0:
                    board.delete_letter()
                    users_word.pop()

            elif command == "ENTER":
                if len(users_word) == 5:
                    board.check_tiles(users_word, word_to_guess)
                    board.next_row()
                    users_word = []

            elif len(command) == 1:
                if len(users_word) < 5:
                    board.change_letter(command)
                    users_word.append(command)

pygame.quit()
