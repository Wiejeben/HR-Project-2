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
        screen.blit(pygame.transform.scale(pself.texture), (self.size.X, self.size.Y), (self.position.X, self.position.Y))