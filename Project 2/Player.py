from Entities import *
from Library.Image import *

class Player:
    def __init__(self, tile, isRealPlayer, color):
        self.isRealPlayer = isRealPlayer
        self.tile = tile
        self.color = color

    def drawPawn(self, position):
        Image("pieces/" + self.color + "/piece.png", 'Game', (position.X, position.Y)).draw()