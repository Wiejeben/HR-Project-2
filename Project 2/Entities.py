import random

class Vector2D():
    def __init__(self, positionX, positionY):
        self.X = positionX
        self.Y = positionY

class Dice():
    def __init__(self, Position, Size):
        self.Number = 1
        self.Position = Position
        self.Size = Size
    def roll(self): 
        self.Number = random.randint(1,6)
    def getTexture(self):
        return {
            1: "Assets/dice/dice_1.png", 
            2: "Assets/dice/dice_2.png",
            3: "Assets/dice/dice_3.png",
            4: "Assets/dice/dice_4.png",
            5: "Assets/dice/dice_5.png",
            6: "Assets/dice/dice_6.png"
        }.get(self.Number, 1)
    def render(self, screen):
        screen.blit(
            pygame.transform.scale(pygame.image.load(self.getTexture).convert_alpha()), 
            (self.Size.X, self.Size.Y), 
            (self.Position.X, self.Position.Y)
        )