from components.tile import Tile

class Row:
    def __init__(self,y):
        self.y = y
        self.tiles = []
        for x in range (130, 470, 60):
            self.tiles.append(Tile(x, self.y))

    def create_row(self, window):
        for i in range(5):
            self.tiles[i].create_tile(window)

    def change_letter(self, index, letter):
        self.tiles[index].change_letter(letter)

    def change_status(self, index, status):
        self.tiles[index].change_status(status)