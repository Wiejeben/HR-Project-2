﻿from Init import *
from Library.Image import *
from Library.Text import *

class Menu:
    def __init__(self):
        global app_state
        self.screen = pygame.display.get_surface()

        self.buttons_index = [
            Image("buttons/Start.png", 'Menu', ('center', 300)).hover("buttons/Start_Active.png").click(None, app_state.start),
            Image("buttons/Rules.png", 'Menu', ('center', 400)).hover("buttons/Rules_Active.png").click(None, app_state.rules),
            Image("buttons/Options.png", 'Menu', ('center', 500)).hover("buttons/Options_Active.png").click(None, app_state.options),
            Image("buttons/Exit.png", 'Menu', ('center', 600)).hover("buttons/Exit_Active.png").click(None, app_state.exit)
        ]

        self.elements_rules = [
            Image("buttons/Rules.png", 'Rules', ('center', 300)).hover("buttons/Rules_Active.png"),
            Image("buttons/Return.png", 'Rules', ('center', 400)).hover("buttons/Return_Active.png").click(None, app_state.menu),
            Text("Rules", 50, (100, 10, 10), ('center', 0))
        ]

        self.elements_options = [
            Image("buttons/Options.png", 'Options', ('center', 300)).hover("buttons/Options_Active.png"),
            Image("buttons/Return.png",  'Options', ('center', 400)).hover("buttons/Return_Active.png").click(None, app_state.menu),
            Text("Opties", 50, (100, 10, 10), ('center', 0))
        ]

    def index(self):
        # Set background color
        pygame.display.get_surface().fill((255, 255, 255))

        for button in self.buttons_index:
            button.draw()

    def rules(self):
        # Set background color
        self.screen.fill((0, 255, 0))

        for element in self.elements_rules:
            element.draw()

    def options(self):
        # Set background color
        self.screen.fill((255, 100, 0))

        for element in self.elements_options:
            element.draw()
