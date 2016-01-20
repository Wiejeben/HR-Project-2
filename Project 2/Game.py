import pygame
from Entities import *
from Player import *
from Node import *

class Game:
    def __init__(self, background, amount_opponents):
        self.background = background
        self.loaded = False
        self.players = []
        self.board = GameBoard(Vector2D(0,0), Vector2D(768,768))
        self.tiles = [
            GameTile(Vector2D(710,720)), 
            GameTile(Vector2D(630,720)), 
            GameTile(Vector2D(570,720)), 
            GameTile(Vector2D(510,720)),
            GameTile(Vector2D(450,720)), 

            GameTile(Vector2D(390,720)), 
            GameTile(Vector2D(330,720)), 
            GameTile(Vector2D(270,720)),
            GameTile(Vector2D(210,720)), 
            GameTile(Vector2D(150,720)), 

            GameTile(Vector2D(60,720)), 
            GameTile(Vector2D(60,610)),
            GameTile(Vector2D(60,550)), 
            GameTile(Vector2D(60,490)), 
            GameTile(Vector2D(60,430)), 

            GameTile(Vector2D(60,370)),
            GameTile(Vector2D(60,310)), 
            GameTile(Vector2D(60,250)), 
            GameTile(Vector2D(60,190)), 
            GameTile(Vector2D(60,130)),

            GameTile(Vector2D(60,60)), 
            GameTile(Vector2D(140,60)), 
            GameTile(Vector2D(210,60)), 
            GameTile(Vector2D(270,60)),
            GameTile(Vector2D(330,60)),

            GameTile(Vector2D(390,60)), 
            GameTile(Vector2D(450,60)), 
            GameTile(Vector2D(510,60)), 
            GameTile(Vector2D(570,60)),
            GameTile(Vector2D(630,60)),

            GameTile(Vector2D(710,60)), 
            GameTile(Vector2D(710,130)), 
            GameTile(Vector2D(710,190)), 
            GameTile(Vector2D(710,250)),
            GameTile(Vector2D(710,310)),

            GameTile(Vector2D(710,370)), 
            GameTile(Vector2D(710,430)), 
            GameTile(Vector2D(710,490)), 
            GameTile(Vector2D(710,550)),
            GameTile(Vector2D(710,610))
        ]
        
        for i in range(1, amount_opponents):
            self.players.append(Player(0))

        for player in self.players:
            player.position = 1

    def renderBoard(self, screen):
        self.board.render(screen)

    def load(self):
        yellow = 255, 255, 0
        self.background.fill(yellow)
        font = pygame.font.Font(None, 36)
        text = font.render("Game", 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = self.background.get_rect().centerx
        self.background.blit(text, textpos)
    def update(self):
        for player in self.players:
           if player.position < 39:
               player.position = player.position + 1
           else:
               player.position = 0
    def drawPlayers(self, screen):
        for player in self.players:
            player.drawPawn(screen, self.tiles[player.position].position)
    def pause(self):
        print("Paused")
        
        orange = 255, 100, 0 
        self.background.fill(orange)
        font = pygame.font.Font(None, 36)
        text = font.render("Paused!", 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = self.background.get_rect().centerx
        self.background.blit(text, textpos)


