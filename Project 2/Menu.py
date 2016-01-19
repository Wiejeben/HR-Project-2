import pygame

class Menu(object):
    def __init__(self, background):
        self.background = background

    def load(self):
        green = 50, 255, 100
        self.background.fill(green)
        font = pygame.font.Font(None, 36)
        text = font.render("Menu", 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = self.background.get_rect().centerx
        self.background.blit(text, textpos)


