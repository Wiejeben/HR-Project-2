from Entities import *

class Player:
    def __init__(self, tile):
        self.isRealPlayer = False
        self.tile = tile
        self.size = Vector2D(64,64)
        self.texture = pygame.image.load("Content/pieces/blue/piece.png").convert_alpha()
    def drawPawn(self, screen, position):
        screen.blit(pygame.transform.scale(self.texture, (self.size.X, self.size.Y)), (position.X - (self.size.X / 2), position.Y - (self.size.Y / 2)))