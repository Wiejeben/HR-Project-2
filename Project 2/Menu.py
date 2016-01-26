from Init import *
from Library.Image import *
from Library.Text import *

class Menu:
    def __init__(self):
        global app_state

        self.buttons_index = [
            Image("buttons/Start.png", 'Menu', ('center', 300)).hover("buttons/Start_Active.png").click(None, app_state.player_select),
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

        self.elements_player_select = [
            #TODO: Give argument for #of players
            Image("buttons/Start.png", 'PlayerSelect', (750, 680)).hover("buttons/Start_Active.png").click(None, app_state.start),
            Image("buttons/Return.png", 'PlayerSelect', (30, 680)).hover("buttons/Return_Active.png").click(None, app_state.menu),
            Image("buttons/checkbox_unchecked.png", 'PlayerSelect', (60, 200)).hover("buttons/checkbox_checked.png").click(None, self.select_checkbox),
            Text("Select amount of AI players", 50, (100,10,10), ('center', 0))
        ]
            

        self.screen = pygame.display.get_surface()

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

    def select_checkbox(self):
        self.elements_player_select[2].visible = False
        #self.elements_player_select.insert(3, Image("buttons/checkbox_checked.png", 'PlayerSelect', (60, 200)).hover("buttons/checkbox_unchecked.png").click(None, self.unselect_checkbox))

    def unselect_checkbox(self):
        self.elements_player_select[2] = Image("buttons/checkbox_unchecked.png", 'PlayerSelect', (60, 200)).hover("buttons/checkbox_checked.png").click(None, self.select_checkbox)
    def playerSelect(self):
        self.screen.fill((255,230,200))

        for element in self.elements_player_select:
            element.draw()
