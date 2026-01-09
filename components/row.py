from components.tile import Tile
from settings import GREEN, YELLOW, DARK_GRAY

class Row:
    def __init__(self,y):
        self.y = y
        self.tiles = []
        self.current_tile = 0
        for x in range (130, 470, 60):
            self.tiles.append(Tile(x, self.y))

    def create_row(self, window):
        for i in range(5):
            self.tiles[i].create_tile(window)

    def change_letter(self, letter):
        if self.current_tile < 5:
            self.tiles[self.current_tile].change_letter(letter)
            self.current_tile += 1

    def delete_letter(self):
        if self.current_tile > 0:
            self.current_tile -= 1
            self.tiles[self.current_tile].delete_letter()

    def check_tiles(self, users_word, word_to_guess):
        for i in range(5):
            if users_word[i] == word_to_guess[i]:
                self.tiles[i].change_color(GREEN)
            elif users_word[i] in word_to_guess:
                self.tiles[i].change_color(YELLOW)
            else:
                self.tiles[i].change_color(DARK_GRAY)


    def get_current_tile(self):
        return self.current_tile