from Entities import *
from Library.Image import *

class Player:
    def __init__(self, tile, isRealPlayer, color):
        self.isRealPlayer = isRealPlayer
        self.tile = tile
        self.color = color
        self.board = PlayerBoard()

    def draw(self, position):
        Image("pieces/" + self.color + "/piece.png", 'Game', (position.X, position.Y)).draw()

class PlayerBoard:
    def __init__(self):
        self.texture = Image("board/player_board.png", 'Game', (117,334), (471,252))
        self.attractions = []
    def getTexture(self):
        return self.texture
    def setAttraction(key, attractionObject):
        self.attractions[key] = attractionObject
    def getAttraction(key):
        return self.attractions[key]
    def draw(self):
        self.texture.draw()