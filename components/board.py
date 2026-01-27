from components.row import Row

class Board:
    def __init__(self):
        self.rows = [] #lista, która przechowuje sześć rzędów
        self.current_row = 0
        for y in range(80, 450, 60):
            self.rows.append(Row(y))

    def create_board(self, window):
        #tworzy wiersze w oknie gry
        for index in range(6):
            self.rows[index].create_row(window)

    def change_letter(self, letter):
        #przekazuje polecenie, aby zmienić literę w danym kafelku
        self.rows[self.current_row].change_letter(letter)

    def next_row(self):
        #przesuwa się do następnego rzędu
        self.current_row += 1

    def delete_letter(self):
        #przekazuje polecenie, aby usunąć ostatnią literę
        self.rows[self.current_row].delete_letter()

    def check_tiles(self, users_word, word_to_guess):
        #sprawdza kolor kafelków w danym wierszu
        self.rows[self.current_row].check_tiles(users_word, word_to_guess)

    def get_current_tile(self):
        #zwraca aktualny kafelek
        return self.rows[self.current_row].get_current_tile()

    def shake_animation(self):
        #uruchamia trzęsienie aktualnym rzędem
        self.rows[self.current_row].shake_animation()

    def get_last_row_results(self):
        #pobiera wyniki z ostatniego rzędu-litery i kolor
        results = []
        # current_row jest już o 1 większy, więc sprawdzamy poprzedni
        last_row = self.rows[self.current_row - 1]
        for i, tile in enumerate(last_row.tiles):
            results.append({
                "index": i,
                "letter": tile.letter.upper(),
                "color": tile.color
            })
        return results