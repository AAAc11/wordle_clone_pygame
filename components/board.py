from components.row import Row

class Board:
    def __init__(self):
        self.rows = []
        self.current_row = 0
        for y in range(80, 450, 60):
            self.rows.append(Row(y))

    def create_board(self, window):
        for index in range(6):
            self.rows[index].create_row(window)

    def change_letter(self, letter):
        self.rows[self.current_row].change_letter(letter)

    def next_row(self):
        self.current_row += 1

    def delete_letter(self):
        self.rows[self.current_row].delete_letter()

    def check_tiles(self, users_word, word_to_guess):
        self.rows[self.current_row].check_tiles(users_word, word_to_guess)

    def get_current_tile(self):
        return self.rows[self.current_row].get_current_tile()

