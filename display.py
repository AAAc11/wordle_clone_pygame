import time
import pygame
from keyboard import keyboard_display, buttons
from rows import LetterArea
from word_of_the_day import word_draw
from game_result import Result

pygame.init()
pygame.font.init()

running = True

############### PARAMETERS ###############
WORDLE_SCREEN_WIDTH = 550
WORDLE_SCREEN_HEIGHT = 700
WINDOW_COLOR = (31, 27, 27)
WHITE = (255, 255, 255)
GREEN = (79, 235, 52)
YELLOW = (235, 214, 52)
GRAY = (61, 64, 69)

############### VARIABLES ###############
grid = []
user_word = []
current_row = 0
current_col = 0
start_x = 130
start_y = 90

font = pygame.font.SysFont(None, 70)
text = font.render('WORDLE', True, WHITE)
main_window = pygame.display.set_mode((WORDLE_SCREEN_WIDTH, WORDLE_SCREEN_HEIGHT))
main_window.fill(WINDOW_COLOR)
pygame.display.set_caption("WORDLE")

word_to_guess = word_draw().strip()
print(word_to_guess)

keyboard_display(main_window)

result_window = Result()

############### LETTER TILES ###############
for row in range(6):
    row_tiles = []
    for col in range(5):
        x = start_x + (col * 60)
        y = start_y + (row * 60)
        new_tile = LetterArea(main_window, x, y)
        row_tiles.append(new_tile)
    grid.append(row_tiles)

start_time = time.perf_counter()

############### MAIN LOOP ###############
while running:
    main_window.fill(WINDOW_COLOR)
    main_window.blit(text, [165, 30])

    for button in buttons.values():
        button.creating_area()

    for row in grid:
        for tile in row:
            tile.letter_display(main_window)


    pygame.display.flip()
    pygame.display.update()

    for event in pygame.event.get():
        clicked_letter = None
        if event.type == pygame.QUIT:
            running = False
        #Physical keyboard
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                clicked_letter = event.unicode.upper()
            elif event.key == pygame.K_BACKSPACE:
                clicked_letter = "REMOVE"
            elif event.key == pygame.K_RETURN:
                clicked_letter = "ENTER"
        #On-screen keyboard
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos

            for button in buttons.values():
                if button.rect.collidepoint(mouse_position) and button.letter:
                    clicked_letter = button.letter

        if clicked_letter:
            if clicked_letter == "ENTER":
                if current_col == 5:
                    for i in range(5):
                        for button in buttons.values():
                            if grid[current_row][i].get_letter() == word_to_guess[i]:
                                grid[current_row][i].set_color(GREEN)
                                if button.letter == grid[current_row][i].get_letter():
                                    button.change_color(GREEN)
                            elif grid[current_row][i].get_letter() in word_to_guess:
                                grid[current_row][i].set_color(YELLOW)
                                if button.letter == grid[current_row][i].get_letter():
                                    button.change_color(YELLOW)
                            else:
                                if button.letter == grid[current_row][i].get_letter():
                                    button.change_color(GRAY)

                    if current_row == 5:
                        end_time = time.perf_counter()
                        gameplay_time = round(end_time - start_time, 2)
                        result_window.printing_result("lose", current_row, gameplay_time, word_to_guess)
                        running = False

                    if "".join(user_word) == word_to_guess:
                        end_time = time.perf_counter()
                        gameplay_time = round(end_time - start_time, 2)
                        result_window.printing_result("win", current_row, gameplay_time, word_to_guess)
                        running = False


                    user_word = []
                    current_row += 1
                    current_col = 0

            elif clicked_letter == "REMOVE" or clicked_letter == "RETURN":
                if current_col > 0:
                    current_col -= 1
                    grid[current_row][current_col].set_letter("")
                    user_word.pop()
            else:
                if current_col < 5:
                    user_word.append(clicked_letter)
                    grid[current_row][current_col].set_letter(clicked_letter)
                    current_col += 1
print(f"guessed password : {word_to_guess}")

pygame.quit()
