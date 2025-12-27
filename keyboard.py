import pygame

pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

rows_of_letters = ['QWERTYUIOP',
                   'ASDFGHJKL',
                   'ZXCVBNM']
buttons = {}

class Button:
    def __init__(self, letter, background_color, width, x, y, font_size, window):
        self.letter =letter
        self.background_color = background_color
        self.width = width
        self.x = x
        self.y = y
        self.font_size = font_size
        self.window = window

    def creating_area(self):
        font = pygame.font.Font(None, self.font_size)
        surface = pygame.draw.rect(self.window, self.background_color, (self.x, self.y, self.width, 55), 0, border_radius=3)
        letter_surface = font.render(self.letter, True, BLACK)
        letter_rect = letter_surface.get_rect(center = surface.center)
        self.window.blit(letter_surface, letter_rect)

    def change_color(self, color):
        self.background_color = color

#rows of letters
def keyboard_display(window):
    start_x_positions = [30, 55, 105]

    for i, (row_letters, y) in enumerate(zip(rows_of_letters, range(450, 591, 70))):
        current_x = start_x_positions[i]

        for letter in row_letters:
            new_letter = Button(letter, WHITE, 40, current_x, y, 35, window)
            buttons[letter] = new_letter
            new_letter.creating_area()
            current_x += 50

    enter = Button('ENTER', WHITE, 65, 30, 590, 20, window)
    enter.creating_area()
    backspace = Button('RETURN', WHITE, 65, 455, 590, 20, window)
    backspace.creating_area()
