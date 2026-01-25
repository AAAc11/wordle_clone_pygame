from components.key import Key
from settings import very_small_font, small_font, DARK_GRAY

class Keyboard:
    def __init__(self):
        self.keys = []

        rows = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
        start_x_position = [30, 55, 105]
        for i, (row_letters, y) in enumerate(zip(rows, range(450, 591, 70))):
            current_x = start_x_position[i]

            for letter in row_letters:
                new_letter = Key(letter, current_x, y, 40, small_font)
                self.keys.append(new_letter)
                current_x += 50

        enter = Key('ENTER', 30, 590, 65, very_small_font)
        self.keys.append(enter)
        backspace = Key('REMOVE', 455, 590, 65, very_small_font)
        self.keys.append(backspace)


    def create_keyboard(self, window):
        for key in self.keys:
            key.create_key(window)

    def which_letter_is_clicked(self, mouse_position):
        for key in self.keys:
            if key.is_clicked(mouse_position):
                return  key.is_clicked(mouse_position)

    def change_color(self, tiles):
        for tile in tiles:
            for key in self.keys:
                if key.get_letter() == tile.get_letter() and key.get_letter() not in ['ENTER', 'REMOVE']:
                    key.change_color(tile.color)