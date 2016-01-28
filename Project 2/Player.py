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

    def calculate_salary(self):
        salary = 0
        for attraction in self.board.attractions:
            salary += (attraction.price / 20)
        self.money += salary

    def buy_attraction(self, attraction, position):
        if self.money > attraction.price:
            self.money -= attraction.price
            self.board.set_attraction(attraction, position)

    def draw(self, position):
        Image("pieces/" + self.color + "/piece.png", 'Game', (position.X, position.Y)).draw()

class PlayerBoard:
    def __init__(self):
        self.texture = Image("board/player_board.png", 'Game', (117,334), (471,252))
        self.attractions = {}
    def getTexture(self):
        return self.texture
    def set_attraction(self, position, attraction):
        self.attractions[position] = attraction
    def get_attraction(key):
        return self.attractions[key]
    def draw(self):
        self.texture.draw()

        i = 0
        for attraction in self.attractions:
            attraction.draw(i)
            i += 1

class Attraction:
    def __init__(self, name, price, type):
        self.name = name
        self.price = price
        self.type = type
    def draw(self, offset):
        if offset < 6:
            Image("attractions/"+ str(self.type) +".png", 'Game', (115 + offset * 80, 330)).draw()
        else:
            Image("attractions/"+ str(self.type) +".png", 'Game', (115 + offset % 6 * 80, 450)).draw()