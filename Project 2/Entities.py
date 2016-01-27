import random
import pygame
from time import sleep
from Library.Image import *

class Vector2D():
    def __init__(self, x, y):
        self.X = x
        self.Y = y
    def __str__(self):
        return "(" + str(self.X) + ", " + str(self.Y) + ")"

class Dice():
    def __init__(self, position, size):
        self.number = 1
        self.position = position
        self.size = size
        self.texture = {
            1 : Image("dice/dice_1.png", 'Game', (self.position.X, self.position.Y)),
            2 : Image("dice/dice_2.png", 'Game', (self.position.X, self.position.Y)),
            3 : Image("dice/dice_3.png", 'Game', (self.position.X, self.position.Y)),
            4 : Image("dice/dice_4.png", 'Game', (self.position.X, self.position.Y)),
            5 : Image("dice/dice_5.png", 'Game', (self.position.X, self.position.Y)),
            6 : Image("dice/dice_6.png", 'Game', (self.position.X, self.position.Y))
        }

    def roll(self): 
        self.number = random.randint(1,6)

    def draw(self):
        self.texture[self.number].draw()

class GameTile:
    def __init__(self, pawnPosition):
        self.position = pawnPosition
 