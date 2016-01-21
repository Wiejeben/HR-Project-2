import pygame
from UIToolKit.Image import *

class Menu:
    def __init__(self, app):

        self.buttons = [
            Image("buttons/Start.png", ('center', 100)).hover("buttons/Start_Active.png").click(app.start),
            Image("buttons/Options.png", ('center', 200)).hover("buttons/Options_Active.png"),
            Image("buttons/Exit.png", ('center', 300)).hover("buttons/Exit_Active.png").click(app.exit)
        ]

    def draw(self):
        # Set background color
        pygame.display.get_surface().fill((255, 255, 255))

        for button in self.buttons:
            button.draw()


