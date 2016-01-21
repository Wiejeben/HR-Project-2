import pygame
from Library.Image import *

class Menu:
    def __init__(self, app):
        self.buttons_index = [
            Image("buttons/Start.png", ('center', 300)).hover("buttons/Start_Active.png").click(app.start),
            Image("buttons/Options.png", ('center', 400)).hover("buttons/Options_Active.png").click(app.options),
            Image("buttons/Exit.png", ('center', 500)).hover("buttons/Exit_Active.png").click(app.exit)
        ]

        self.buttons_rules = [
            Image("buttons/Exit.png", ('center', 300)).hover("buttons/Options_Active.png")
        ]

        self.buttons_options = [
            Image("buttons/Options.png", ('center', 300)).hover("buttons/Exit_Active.png")
        ]

    def index(self):
        # Set background color
        pygame.display.get_surface().fill((255, 255, 255))

        for button in self.buttons_index:
            button.draw()

    def rules(self):
        # Set background color
        pygame.display.get_surface().fill((255, 255, 255))

        for button in self.buttons_rules:
            button.draw()

    def options(self):
        # Set background color
        pygame.display.get_surface().fill((255, 255, 255))

        for button in self.buttons_options:
            button.draw()
