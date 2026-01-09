from components.key import Key
from settings import very_small_font, small_font

class Keyboard:
    def __init__(self):
        self.keys = []


    def create_keyboard(self, window):
        rows = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
        start_x_position = [30, 55, 105]
        for i, (row_letters, y) in enumerate(zip(rows, range(450, 591, 70))):
            current_x = start_x_position[i]

            for letter in row_letters:
                new_letter = Key(letter, current_x, y, 40, small_font)
                self.keys.append(new_letter)
                new_letter.create_key(window)
                current_x += 50

        enter = Key('ENTER',30, 590, 65, very_small_font)
        self.keys.append(enter)
        enter.create_key(window)
        backspace = Key('REMOVE',455, 590, 65, very_small_font)
        self.keys.append(backspace)
        backspace.create_key(window)

    def which_letter_is_clicked(self, mouse_position):
        for key in self.keys:
            if key.is_clicked(mouse_position):
                return  key.is_clicked(mouse_position)