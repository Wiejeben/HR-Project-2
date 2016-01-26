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
        self.texture = []

        for i in range(1, 6):
            self.texture.append(Image("dice/dice_" + str(i) + ".png", 'Game', (self.position.X, self.position.Y)))

    def roll(self): 
        self.number = random.randint(1,6)

    def draw(self):
        self.texture[self.number - 1].draw()

class GameTile:
    def __init__(self, pawnPosition):
        self.position = pawnPosition
 
# DEPRECATED
class PlayerBoard:
    def __init__(self, position, size):
        self.position = position
        self.size = size
        self.texture = pygame.image.load("Content/board/player_board.png").convert_alpha()
        self.attractions = []
    def getTexture(self):
        return self.texture
    def setAttraction(key, attractionObject):
        self.attractions[key] = attractionObject
    def getAttraction(key):
        return self.attractions[key]
    def render(self, screen):
        screen.blit(pygame.transform.scale(self.texture, (self.size.X, self.size.Y)), (self.position.X, self.position.Y))