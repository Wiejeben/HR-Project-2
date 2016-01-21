from Entities import *

class Player:
    def __init__(self, tile, isRealPlayer, color, offset):
        self.isRealPlayer = isRealPlayer
        self.tile = tile
        self.offset = offset
        self.size = Vector2D(64, 64)
        self.color = color
        self.cash = 10000
        self.turn_state = 0
        self.texture = pygame.image.load("Content/pieces/"+color+"/piece.png").convert_alpha()
    def drawPawn(self, screen, position):
        if self.position < 10:
            screen.blit(pygame.transform.scale(self.texture, (self.size.X, self.size.Y)), (position.X - (self.size.X / 2), position.Y - (self.size.Y / 2) + self.offset * 30))
        elif self.position < 20:
            screen.blit(pygame.transform.scale(self.texture, (self.size.X, self.size.Y)), (position.X - (self.size.X / 2) - self.offset * 5, position.Y - (self.size.Y / 2) ))
        elif self.position < 30:
            screen.blit(pygame.transform.scale(self.texture, (self.size.X, self.size.Y)), (position.X - (self.size.X / 2), position.Y - (self.size.Y / 2) + self.offset * 5))
        else:
            screen.blit(pygame.transform.scale(self.texture, (self.size.X, self.size.Y)), (position.X - (self.size.X / 2), position.Y - (self.size.Y / 2) + self.offset * 30))