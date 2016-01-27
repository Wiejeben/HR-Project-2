from Entities import *
from Library.Image import *

class Player:
    def __init__(self, tile, isRealPlayer, color):
        self.isRealPlayer = isRealPlayer
        self.tile = tile
        self.color = color
        self.position = 0
        self.board = PlayerBoard()

    def interact(self, interaction):
        if interaction == 'ThrillRides':
            print ("ThrillRides")
            pass
        elif interaction == 'ShopsAndStalls':
            print ("ShopsAndStalls")
            pass
        elif interaction == 'TransportRides':
            print ("TransportRides")
            pass
        elif interaction == 'WaterRides':
            print ("WaterRides")
            pass
        elif interaction == 'GentleRides':
            print ("GentleRides")
            pass
        elif interaction == 'Rollercoasters':
            print ("Rollercoasters")
            pass
        elif interaction == 'QuestionMark':
            print ("QuestionMark")
            pass
        elif interaction == 'CashFine':
            pass
        elif interaction == 'Start':
            pass
        elif interaction == 'Spectator':
            pass
        elif interaction == 'CashPrize':
            pass
        elif interaction == 'Defect':
            pass

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

class Attraction:
    def __init__(self, name, price):
        self.name = name
        self.price = price
