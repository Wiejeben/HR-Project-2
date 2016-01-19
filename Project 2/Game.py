import pygame
from Entities import *
from Player import *

class Game:
    def __init__(self, background, amount_opponents):
        self.background = background
        self.Players = []
        for i in range(1, amount_opponents):
            self.Players.append(Player())

        self.setupLayout()
    def setupLayout(self):
        pass

    def render(self, screen):
        board = GameBoard(Vector2D(0,0), Vector2D(400,400))
        board.render(screen)
    def load(self):
        yellow = 255, 255, 0
        self.background.fill(yellow)
        font = pygame.font.Font(None, 36)
        text = font.render("Game", 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = self.background.get_rect().centerx
        self.background.blit(text, textpos)

    def pause(self):
        print("Paused")
        
        orange = 255, 100, 0 
        self.background.fill(orange)
        font = pygame.font.Font(None, 36)
        text = font.render("Paused!", 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = self.background.get_rect().centerx
        self.background.blit(text, textpos)


