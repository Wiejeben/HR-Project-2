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

    def buy_attraction(self, attraction):
        if self.money > attraction.price:
            self.money -= attraction.price
            self.board.add_attraction(attraction)

    def draw(self, position):
        Image("pieces/" + self.color + "/piece.png", 'Game', (position.X, position.Y)).draw()

class PlayerBoard:
    def __init__(self):
        self.texture = Image("board/player_board.png", 'Game', (117,334), (471,252))
        self.attractions = [
            Attraction('Bobsleigh Coaster', 18000)
        ]
    def getTexture(self):
        return self.texture
    def add_attraction(self, attraction):
        self.attractions.append(attraction)
    def get_attraction(key):
        return self.attractions[key]
    def draw(self):
        self.texture.draw()

        i = 0
        for attraction in self.attractions:
            attraction.draw(i)
            i += 1

class Attraction:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def draw(self, offset):
        Image("attractions/gentle_rides.png", 'Game', (115 + offset * 80, 350)).draw()
