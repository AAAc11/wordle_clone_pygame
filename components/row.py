from components.tile import Tile
from settings import *
import settings

class Row:
    def __init__(self,y):
        self.y = y
        self.tiles = [] #lista, która przechowuje 5 kafelków
        self.current_tile = 0

        for x in range (130, 470, 60):
            self.tiles.append(Tile(x, self.y))

    def create_row(self, window):
        #wywołuje metodę rysowania dla kafelków w rzędzie
        for i in range(5):
            self.tiles[i].create_tile(window)

    def change_letter(self, letter):
        #dodaje literę do kolejnego wolnego kafelka
        if self.current_tile < 5:
            self.tiles[self.current_tile].change_letter(letter)
            self.current_tile += 1

    def delete_letter(self):
        #usuwa ostatnio wpisaną literę
        if self.current_tile > 0:
            self.current_tile -= 1
            self.tiles[self.current_tile].delete_letter()

    def check_tiles(self, users_word, word_to_guess):
        #sprawdzenie słowa i zmiana kolorów kafelków
        for i in range(5):
            if users_word[i] == word_to_guess[i]:
                self.tiles[i].change_color(GREEN)
            elif users_word[i] in word_to_guess:
                self.tiles[i].change_color(YELLOW)
            else:
                if not settings.IS_DARK_MODE:
                    self.tiles[i].change_color((120, 124, 126))
                else:
                    self.tiles[i].change_color(DARK_GRAY)


    def get_current_tile(self):
        return self.current_tile

    def shake_animation(self):
        #uruchamia animację trzęsienia w rzędzie
        for tile in self.tiles:
            tile.start_shake()