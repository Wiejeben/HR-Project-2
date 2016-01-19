import pygame
from * import Entities

class Game(object):
    def __init__(self, amount_opponents):
        self.background = background
        self.Players = {}
        for i in list(1, amount_opponents):
            self.Players.insert(Player())

        self.setupLayout()
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


