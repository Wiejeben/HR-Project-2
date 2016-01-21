from Entities import *

class Player:
    def __init__(self, tile, isRealPlayer, color):
        self.isRealPlayer = isRealPlayer
        self.tile = tile
        self.size = Vector2D(128, 128)
        self.color = color
        self.texture = pygame.image.load("Content/pieces/"+color+"/piece.png").convert_alpha()

    def drawPawn(self, screen, position):
        screen.blit(pygame.transform.scale(self.texture, (self.size.X, self.size.Y)), (position.X - (self.size.X / 2), position.Y - (self.size.Y / 2)))