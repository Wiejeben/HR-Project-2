import pygame
from Library.Image import *
from Init import *

class Menu:
    def __init__(self):
        global app_state

        self.buttons_index = [
            Image("buttons/Start.png", ('center', 300)).hover("buttons/Start_Active.png", 'Menu').click(app_state.start),
            Image("buttons/Rules.png", ('center', 400)).hover("buttons/Rules_Active.png", 'Menu').click(app_state.rules),
            Image("buttons/Options.png", ('center', 500)).hover("buttons/Options_Active.png", 'Menu').click(app_state.options),
            Image("buttons/Exit.png", ('center', 600)).hover("buttons/Exit_Active.png", 'Menu').click(app_state.exit)
        ]

        self.buttons_rules = [
            Image("buttons/Rules.png", ('center', 300)).hover("buttons/Rules_Active.png", 'Rules'),
            Image("buttons/Return.png", ('center', 400)).hover("buttons/Return_Active.png", 'Rules').click(app_state.menu)
        ]

        self.buttons_options = [
            Image("buttons/Options.png", ('center', 300)).hover("buttons/Options_Active.png", 'Options'),
            Image("buttons/Return.png", ('center', 400)).hover("buttons/Return_Active.png", 'Options').click(app_state.menu)
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
