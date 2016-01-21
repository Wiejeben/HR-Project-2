import pygame
from Entities import *
from Player import *

class Game:
    def __init__(self, amount_opponents):
        self.screen = pygame.display.get_surface()
        self.players = []
        for i in range(1, amount_opponents):
            self.players.append(Player())

        self.setupLayout()
    def setup_layout(self):
        pass

    def render(self, screen):
        board = GameBoard(Vector2D(0,0), Vector2D(400,400))
        board.render(screen)

    def load(self):
        yellow = 255, 255, 0
        self.screen.fill(yellow)

        font = pygame.font.Font(None, 36)
        text = font.render("Game", 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = self.screen.get_rect().centerx
        self.screen.blit(text, textpos)

    def pause(self):
        print("Paused")
        
        orange = 255, 100, 0 
        self.screen.fill(orange)
        font = pygame.font.Font(None, 36)
        text = font.render("Paused!", 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = self.screen.get_rect().centerx
        self.screen.blit(text, textpos)


