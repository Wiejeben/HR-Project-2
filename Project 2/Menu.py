from Init import *
from Library.Image import *
from Library.Text import *

class Menu:
    def __init__(self):
        global app_state

        self.screen = pygame.display.get_surface()
        self.amount_of_human_players = 0
        self.human_players = [False, False, False, False]
        self.sound_state = True

        self.buttons_index = [
            Image("board/Logo.png", 'Menu', ('center', 20)),
            Image("buttons/Start.png", 'Menu', ('center', 350)).hover("buttons/Start_Active.png").click(None, app_state.player_select),
            Image("buttons/Rules.png", 'Menu', ('center', 450)).hover("buttons/Rules_Active.png").click(None, app_state.rules),
            Image("buttons/Options.png", 'Menu', ('center', 550)).hover("buttons/Options_Active.png").click(None, app_state.options),
            Image("buttons/Exit.png", 'Menu', ('center', 650)).hover("buttons/Exit_Active.png").click(None, app_state.exit)
        ]

        self.elements_rules = [
            Text("Rules", 50, (100, 10, 10), ('center', 210)),

            # Rules text
            Text("This game is a strategy, competitive, chance and class/level based board game.", 22, (0, 0, 0), ('center', 260)),
            Text("The mainboard has some elements of Monopoly in it, but we changed it up so much that you can’t call it’s a Monopoly rip-off.", 22, (0, 0, 0), ('center', 280)),
            Text("It’s actually a game with elements of RollercoasterTycoon and Levensweg in it as well.", 22, (0, 0, 0), ('center', 300)),
            Text("That makes it a game that is appealing for people that like to sit down for a nice board game and really get involved in", 22, (0, 0, 0), ('center', 320)), 
            Text("-what they are building but it’s also a great game to play with the family.", 22, (0, 0, 0), ('center', 340)),
            Text("Yes, you “build” your own amusement park in this board game.", 22, (0, 0, 0), ('center', 360)),
            Text("Including all the categories from RollercoasterTycoon, income based on guests, challenges and much, much more.", 22, (0, 0, 0), ('center', 380)),
            Text("Dive into the world of The Ultimate Combination.", 22, (0, 0, 0), ('center', 400)),
            Text("Have Fun!", 30, (0, 0, 0), ('center', 450)),

            Image("buttons/Return.png", 'Rules', ('center', 500)).hover("buttons/Return_Active.png").click(None, app_state.menu)
        ]

        self.elements_options = [
            Text("Sound", 40, (0,0,0), (450, 200)),
            Image("buttons/checkbox_checked.png", 'Options', (575, 185)).toggle("buttons/checkbox_unchecked.png", self.sound_toggle),         
            Image("buttons/Return.png",  'Options', (30, 680)).hover("buttons/Return_Active.png").click(None, app_state.menu),
            Text("Options", 50, (100, 10, 10), ('center', 10))
        ]

        self.elements_player_select = {
            'checkboxes': (
                Image("buttons/checkbox_unchecked.png", 'PlayerSelect', (210, 200)).toggle("buttons/checkbox_checked.png", self.select_players, 0),                
                Image("buttons/checkbox_unchecked.png", 'PlayerSelect', (210, 260)).toggle("buttons/checkbox_checked.png", self.select_players, 1),
                Image("buttons/checkbox_unchecked.png", 'PlayerSelect', (210, 320)).toggle("buttons/checkbox_checked.png", self.select_players, 2),
                Image("buttons/checkbox_unchecked.png", 'PlayerSelect', (210, 380)).toggle("buttons/checkbox_checked.png", self.select_players, 3)
            ),

            'checkboxes_labels': (
                Text("Player 1: ", 60, (0,0,0), (10, 205)),
                Text("Player 2: ", 60, (0,0,0), (10, 265)),
                Text("Player 3: ", 60, (0,0,0), (10, 325)),
                Text("Player 4: ", 60, (0,0,0), (10, 385))
            ),

            'buttons': (
                Image("buttons/Start.png", 'PlayerSelect', (900, 680)).hover("buttons/Start_Active.png").click(None, app_state.start, self.human_players),
                Image("buttons/Return.png", 'PlayerSelect', (30, 680)).hover("buttons/Return_Active.png").click(None, app_state.menu)
            ),
            'amount': Text("Human players: " + str(self.amount_of_human_players), 50, (100,10,10), ('center', 690)),

            'misc': (Text("Select amount of Human players", 50, (0,0,0), ('center', 150)))
        }        

    def index(self):
        # Set background color
        pygame.display.get_surface().fill((255, 255, 255))

        for button in self.buttons_index:
            button.draw()

    def rules(self):
        # Set background color
        self.screen.fill((255, 255, 255))

        for element in self.elements_rules:
            element.draw()

    def options(self):
        # Set background color
        self.screen.fill((255, 255, 255))

        for element in self.elements_options:
            element.draw()

    def select_players(self, player_joined):
       self.human_players[player_joined] = not self.human_players[player_joined]
      
       self.amount_of_human_players = 0 
       for elem in self.human_players:
           if(elem):
               self.amount_of_human_players += 1

       self.elements_player_select['amount'].set_text("Human players: " + str(self.amount_of_human_players))

    def sound_toggle(self):
        self.sound_state = not self.sound_state
        app_state.sound(self.sound_state)

    def playerSelect(self):
        self.screen.fill((255,230,200))

        for key, val in self.elements_player_select.items():
            if type(val) is tuple:
                for val in val:
                    val.draw()
            else:
                val.draw()
