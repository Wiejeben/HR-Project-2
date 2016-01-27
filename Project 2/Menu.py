from Init import *
from Library.Image import *
from Library.Text import *

class Menu:
    def __init__(self):
        global app_state

        self.screen = pygame.display.get_surface()
        self.amount_of_human_players = 0
        self.human_players = [False, False, False, False]

        self.buttons_index = [
            Image("buttons/Start.png", 'Menu', ('center', 300)).hover("buttons/Start_Active.png").click(None, app_state.player_select),
            Image("buttons/Rules.png", 'Menu', ('center', 400)).hover("buttons/Rules_Active.png").click(None, app_state.rules),
            Image("buttons/Options.png", 'Menu', ('center', 500)).hover("buttons/Options_Active.png").click(None, app_state.options),
            Image("buttons/Exit.png", 'Menu', ('center', 600)).hover("buttons/Exit_Active.png").click(None, app_state.exit)
        ]

        self.elements_rules = [
            Image("buttons/Return.png", 'Rules', ('center', 500)).hover("buttons/Return_Active.png").click(None, app_state.menu),
            Text("Rules", 50, (100, 10, 10), ('center', 10)),
            Text("This game is a strategy, competitive, chance and class/level based board game.", 22, (0, 0, 0), ('center', 60)),
            Text("The mainboard has some elements of Monopoly in it, but we changed it up so much that you can’t call it’s a Monopoly rip-off.", 22, (0, 0, 0), ('center', 80)),
            Text("It’s actually a game with elements of RollercoasterTycoon and Levensweg in it as well.", 22, (0, 0, 0), ('center', 100)),
            Text("That makes it a game that is appealing for people that like to sit down for a nice board game and really get involved in", 22, (0, 0, 0), ('center', 120)), 
            Text("-what they are building but it’s also a great game to play with the family.", 22, (0, 0, 0), ('center', 140)),
            Text("Yes, you “build” your own amusement park in this board game.", 22, (0, 0, 0), ('center', 160)),
            Text("Including all the categories from RollercoasterTycoon, income based on guests, challenges and much, much more.", 22, (0, 0, 0), ('center', 180)),
            Text("Dive into the world of The Ultimate Combination.", 22, (0, 0, 0), ('center', 200)),
            Text("Have Fun!", 30, (0, 0, 0), ('center', 250))
        ]

        self.elements_options = [
            Image("buttons/Return.png",  'Options', ('center', 400)).hover("buttons/Return_Active.png").click(None, app_state.menu),
            Text("Opties", 50, (100, 10, 10), ('center', 0))
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
                Image("buttons/Start.png", 'PlayerSelect', (750, 680)).hover("buttons/Start_Active.png").click(None, app_state.start),
                Image("buttons/Return.png", 'PlayerSelect', (30, 680)).hover("buttons/Return_Active.png").click(None, app_state.menu)
            ),
            'amount': Text("Human players: " + str(self.amount_of_human_players), 50, (100,10,10), (330, 690)),

            'misc': (Text("Select amount of Human players", 50, (100,10,10), ('center', 5)))
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
       if(player_joined == 0):
           self.human_players[0] = not self.human_players[0]
       elif(player_joined == 1):
           self.human_players[1] = not self.human_players[1]
       elif(player_joined == 2):
           self.human_players[2] = not self.human_players[2]
       elif(player_joined == 3):
           self.human_players[3] = not self.human_players[3]
      
       counter = 0 
       for elem in self.human_players:
           if(elem):
               counter += 1

       self.amount_of_human_players = counter

       self.elements_player_select['amount'].set_text("Human players: " + str(self.amount_of_human_players))


    def playerSelect(self):
        self.screen.fill((255,230,200))

        for key, val in self.elements_player_select.items():
            if type(val) is tuple:
                for val in val:
                    val.draw()
            else:
                val.draw()
