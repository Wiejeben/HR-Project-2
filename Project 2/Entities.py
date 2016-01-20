import random
import pygame

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
    def roll(self): 
        self.number = random.randint(1,6)
    def getTexture(self):
        return pygame.image.load({
            1: "Content/dice/dice_1.png", 
            2: "Content/dice/dice_2.png",
            3: "Content/dice/dice_3.png",
            4: "Content/dice/dice_4.png",
            5: "Content/dice/dice_5.png",
            6: "Content/dice/dice_6.png"
        }.get(self.number, 1)).convert_alpha()
    def render(self, screen):
        screen.blit(pygame.transform.scale(self.getTexture(), (self.size.X, self.size.Y)), (self.position.X, self.position.Y))

class GameBoard:
    def __init__(self, position, size):
        self.position = position
        self.size = size
        self.texture = pygame.image.load("Content/board/game_board.png").convert_alpha()
    def getTexture(self):
        return self.texture
    def render(self, screen):
        screen.blit(pygame.transform.scale(self.texture, (self.size.X, self.size.Y)), (self.position.X, self.position.Y))

class GameTile:
    def __init__(self, pawnPosition):
        self.position = pawnPosition
 
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