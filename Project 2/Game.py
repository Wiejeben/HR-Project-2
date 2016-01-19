import pygame

class Game(object):
    def __init__(self, background):
        self.background = background

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


