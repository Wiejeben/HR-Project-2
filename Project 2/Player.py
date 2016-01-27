from Entities import *
from Library.Image import *

class Player:
    def __init__(self, tile, isRealPlayer, color):
        self.isRealPlayer = isRealPlayer
        self.tile = tile
        self.color = color
        self.position = 0
        self.money = 10000
        self.board = PlayerBoard()

    def calc_salary(self):
        salary = 0
        for i, value in self.board.attractions:
            salary += (value.price / 20)
        print(salary)

    def draw(self, position):
        Image("pieces/" + self.color + "/piece.png", 'Game', (position.X, position.Y)).draw()

class PlayerBoard:
    def __init__(self):
        self.texture = Image("board/player_board.png", 'Game', (117,334), (471,252))
        self.attractions = []
    def getTexture(self):
        return self.texture
    def set_attraction(key, attractionObject):
        self.attractions[key] = attractionObject
    def get_attraction(key):
        return self.attractions[key]
    def draw(self):
        self.texture.draw()

class Attraction:
    def __init__(self, name, price):
        self.name = name
        self.price = price
