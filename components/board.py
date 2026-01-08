from components.row import Row

class Board:
    def __init__(self):
        self.rows = []
        for y in range(90, 450, 60):
            self.rows.append(Row(y))

    def create_board(self, window):
        for index in range(6):
            self.rows[index].create_row(window)

    def change_letter(self, row, index, letter):
        self.rows[row].change_letter(index, letter)

    def change_status(self, row, index, status):
        self.rows[row].change_status(index, status)

