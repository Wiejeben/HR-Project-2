import pygame
from time import sleep
from Entities import *
from Player import *
from Library.Image import *
from Library.Text import *

class Game:
    def __init__(self, human_players):
        self.screen = pygame.display.get_surface()
        self.winning_player = None
        self.elements_won = None
        
        # Load global variables
        global event_handler, app_state
        self.event_handler = event_handler
        self.app_state = app_state

        # Initialize music
        pygame.mixer.music.load("Content/sounds/Track1.wav")
        pygame.mixer.music.play(-1, 0.0)

        # Animation speeds
        self.settings = {
            'pawn_speed' : 800,
            'dice_roll_duration' : 2500,
            'interaction_duration' : 7500,
            'endturn_duration' : 1500
        }

        # Current turn variables
        self.turn_state = {
            'active_player_index'   : 0,
            'state'                 : 'Dice',
            'dice_rolled_tickstart' : 0,
            'dice_score'            : 0,
            'steps_taken'           : 0,
            'steps_taken_tickstart' : 0,
            'start_position'        : 0,
            'interaction'           : False,
            'show_card'             : 0,
            'interaction_tickstart' : 0,
            'endturn_tickstart'     : 0,
        }

        # Some temp tile positions
        bottom_y = 600
        left_x = 5
        top_y = 5
        right_x = 667

        # Board tiles
        self.tiles = [
            # Bottom
            GameTile(Vector2D(640,bottom_y), 'Start'), 
            GameTile(Vector2D(558,bottom_y), 'Rollercoasters', 'attraction'), 
            GameTile(Vector2D(503,bottom_y), 'WaterRides', 'attraction'),
            GameTile(Vector2D(448,bottom_y), 'QuestionMark'),
            GameTile(Vector2D(393,bottom_y), 'ShopsAndStalls', 'attraction'),
            GameTile(Vector2D(338,bottom_y), 'CashFine'),
            GameTile(Vector2D(283,bottom_y), 'TransportRides', 'attraction'),
            GameTile(Vector2D(228,bottom_y), 'QuestionMark'),
            GameTile(Vector2D(173,bottom_y), 'ThrillRides', 'attraction'),
            GameTile(Vector2D(118,bottom_y), 'GentleRides', 'attraction'),
            GameTile(Vector2D(35,bottom_y), 'Spectator'),

            # Left
            GameTile(Vector2D(left_x,542), 'TransportRides', 'attraction'),
            GameTile(Vector2D(left_x,488), 'GentleRides', 'attraction'), 
            GameTile(Vector2D(left_x,434), 'QuestionMark'),
            GameTile(Vector2D(left_x,379), 'Rollercoasters', 'attraction'), 
            GameTile(Vector2D(left_x,323), 'CashFine'),
            GameTile(Vector2D(left_x,268), 'ThrillRides', 'attraction'), 
            GameTile(Vector2D(left_x,214), 'QuestionMark'),
            GameTile(Vector2D(left_x,159), 'ShopsAndStalls', 'attraction'),
            GameTile(Vector2D(left_x,105), 'WaterRides', 'attraction'),

            # Top
            GameTile(Vector2D(35,top_y), 'CashPrize'),
            GameTile(Vector2D(118,top_y), 'WaterRides', 'attraction'),
            GameTile(Vector2D(173,top_y), 'ThrillRides', 'attraction'),
            GameTile(Vector2D(228,top_y), 'QuestionMark'),
            GameTile(Vector2D(283,top_y), 'GentleRides', 'attraction'),
            GameTile(Vector2D(338,top_y), 'CashFine'), 
            GameTile(Vector2D(393,top_y), 'ShopsAndStalls', 'attraction'), 
            GameTile(Vector2D(448,top_y), 'QuestionMark'), 
            GameTile(Vector2D(503,top_y), 'Rollercoasters', 'attraction'),
            GameTile(Vector2D(558,top_y), 'GentleRides', 'attraction'),
            GameTile(Vector2D(640,top_y), 'Defect'),

            # Right
            GameTile(Vector2D(right_x,105), 'ShopsAndStalls', 'attraction'),
            GameTile(Vector2D(right_x,159), 'WaterRides', 'attraction'), 
            GameTile(Vector2D(right_x,214), 'QuestionMark'),
            GameTile(Vector2D(right_x,268), 'ThrillRides', 'attraction'),
            GameTile(Vector2D(right_x,323), 'CashFine'),
            GameTile(Vector2D(right_x,379), 'Rollercoasters', 'attraction'),
            GameTile(Vector2D(right_x,434), 'QuestionMark'),
            GameTile(Vector2D(right_x,488), 'GentleRides', 'attraction'),
            GameTile(Vector2D(right_x,542), 'ThrillRides', 'attraction')
        ]

        self.chance_cards = [
            ChanceCard('cards/card01.png', -5000),
            ChanceCard('cards/card02.png', -6000),
            ChanceCard('cards/card03.png', -10000),
            ChanceCard('cards/card04.png', 2000),
            ChanceCard('cards/card05.png', -3000),
            ChanceCard('cards/card06.png', -4000),
            ChanceCard('cards/card07.png', -3000),
            ChanceCard('cards/card08.png', -2000),
            ChanceCard('cards/card10.png', 2000),
            ChanceCard('cards/card11.png', -3000),
            ChanceCard('cards/card12.png', -7000),
            ChanceCard('cards/card17.png', -6000),
            ChanceCard('cards/card19.png', 1500),
            ChanceCard('cards/card21.png', -2000),
            ChanceCard('cards/card22.png', 3000),
            ChanceCard('cards/card23.png', 3000),
            ChanceCard('cards/card24.png', 3000),
            ChanceCard('cards/card25.png', 2500),
            ChanceCard('cards/card26.png', 1500),
            ChanceCard('cards/card28.png', -5000),
        ]

        # TODO: Implement other attractions
        # self.attractions = [
        #     Attraction('3D Cinema', 10000, 'thrill_rides'),
        #     Attraction('Boat Hire', 3000, 'water_rides'),
        #     Attraction('Train', 5000, 'transport_rides'),
        #     Attraction('Maze', 7500, 'gentle_rides'),
        #     Attraction('Mine Train Coaster', 12500, 'rollercoaster'),
        #     Attraction('Balloon Stall', 1900, 'shops_and_stalls'),

        #     Attraction('Monorail', 12000, 'transport_rides'),
        #     Attraction('Chairlift', 8000, 'transport_rides'),

        #     Attraction('Haunted House', 3500, 'gentle_rides'),
        #     Attraction('Ferriswheel', 6000, 'gentle_rides'),
        #     Attraction('Merrie-go-round', 3000, 'gentle_rides'),
        #     Attraction('Dodgems', 7000, 'gentle_rides'),
        #     Attraction('Monster Trucks', 10000, 'gentle_rides'),
        #     Attraction('Racing Cars', 11000, 'gentle_rides'),
        #     Attraction('Circus', 4000, 'gentle_rides'),
        #     Attraction('Minigold', 8000, 'gentle_rides'),
        #     Attraction('Observation Tower', 15000, 'gentle_rides'),
        #     Attraction('Spiral Slide', 2500, 'gentle_rides'),

        #     Attraction('Bobsleigh Coaster', 18000, 'rollercoaster'),
        #     Attraction('Corkscrew Rollercoaster', 25000, 'rollercoaster'),
        #     Attraction('Giga Coaster', 27000, 'rollercoaster'),
        #     Attraction('Junior Rollercoaster', 7500, 'rollercoaster'),
        #     Attraction('Looping Rollercoaster', 20000, 'rollercoaster'),
            
        #     Attraction('Stand-up Rollercoaster', 19000, 'rollercoaster'),
        #     Attraction('Steel Twister Rollercoaster', 30000, 'rollercoaster'),
        #     Attraction('Wild Mouse', 6500, 'rollercoaster'),
        #     Attraction('Wooden Rollercoaster', 10000, 'rollercoaster'),
        # ]

        self.elements_pause = [
            Text("Pause menu", 50, (255, 255, 255), ('center', 230)),

            Image("buttons/Resume.png",  'Pause', ('center', 300)).hover("buttons/Resume_Active.png").click(None, app_state.pause),
            Image("buttons/Menu.png",  'Pause', ('center', 400)).hover("buttons/Menu_Active.png").click(None, app_state.menu),
            Image("buttons/Exit.png", 'Pause', ('center', 500)).hover("buttons/Exit_Active.png").click(None, app_state.exit)
        ]

        # Load players
        players = []
        for index, isRealPlayer in enumerate(human_players, start=0):
            player = Player(isRealPlayer, index)

            # Set first player to be active
            if index == 0:
                player.isActive = True

            players.append(player)

        # Visible elements
        self.entities = {
            'board': Image("board/game_board.png", 'Game', (0,0), (700,700)),
            'players': players,
            'dice': Dice(Vector2D(135,250), Vector2D(64, 64)),
            'game_rules': Image("board/Help_Text.png", "Game", (180, 400)),
            'buttons' : {
                'button_roll_dice' : Image("buttons/Roll.png", 'Game', (130,140)).hover("buttons/Roll_Active.png").click(None, self.dice_click),
                'help_button' : Image("board/Help.png", 'Game', (520,105)).toggle("board/Help_Active.png", app_state.game_rules),
                'buy' : Image("buttons/Buy.png", 'Game', (5, 705)).hover("buttons/Buy_Active.png"),
                'skip' : Image("buttons/Skip.png", 'Game', (450, 705)).hover("buttons/Skip_Active.png").click(None, self.attraction_skip)
            }
        }

    def get_active_player(self):
        for player in self.entities['players']:
            if player.isActive:
                return player

    def next_turn(self):
        # Reset turn variables
        self.turn_state = {
            'active_player_index'   : (self.turn_state['active_player_index'] + 1) % len(self.entities['players']), # Go to the next player
            'state'                 : 'Dice',
            'dice_rolled_tickstart' : 0,
            'dice_score'            : 0,
            'steps_taken'           : 0,
            'steps_taken_tickstart' : 0,
            'player_start_position' : 0,
            'interaction'           : False,
            'show_card'             : 0,
            'interaction_tickstart' : 0,
            'endturn_tickstart'     : 0
        }

        # Set next player to be active
        for index, player in enumerate(self.entities['players']):
            if index == self.turn_state['active_player_index']:
                player.isActive = True
            else:
                player.isActive = False

    def dice_click(self):
        self.turn_state['dice_rolled_tickstart'] = pygame.time.get_ticks()

    # Attraction methods
    def attraction_event(self, attraction):
        if attraction.owner == None:
            # Buy attraction
            self.attraction_buy(attraction)
        else:
            print("Owned by " + attraction.owner.color)

    def attraction_buy(self, attraction):
        player = self.get_active_player()

        # First see if player has enough money
        if player.money >= attraction.price:
            # Store attraction that we are trying to buy
            self.turn_state['state'] = "BuyAttraction"
            self.turn_state['interaction'] = attraction

            if not player.isRealPlayer: # IF AI
                # 80% odds that the AI is going to buy
                if random.randint(0,10) < 8:
                    print("Buy attraction")
                    self.attraction_buy_confirmed()
                else:
                    print("Skip attraction")
                    self.attraction_skip()
            else:
                # Setup buy click event
                self.entities['buttons']['buy'].click(None, self.attraction_buy_confirmed)

    def attraction_buy_confirmed(self):
        if self.turn_state['state'] == "BuyAttraction":
            self.get_active_player().attraction_buy(self.turn_state['interaction'])
            self.attraction_skip()

    def attraction_skip(self):
        if self.turn_state['state'] == "BuyAttraction":
            
            # Reset click action
            self.entities['buttons']['buy'].click()
            self.turn_state['state'] = 'EndTurn'

    def tile_trigger(self, tile):
        player = self.get_active_player()

        #Debug
        # print(interaction)

        if tile.type == 'attraction':
            self.attraction_event(tile.entity)

        elif tile.interaction == 'QuestionMark':
            self.turn_state['show_card'] = random.choice(self.chance_cards)
            player.money += self.turn_state['show_card'].money
            self.turn_state['interaction_tickstart'] = pygame.time.get_ticks()

        elif tile.interaction == 'CashFine':
            player.calculate_player_class()

            if player.player_class >= 2:
                print("Fined player money")
                player.money -= 5000
            else:
                print("Player class too low")

        elif tile.interaction == 'Start':
            player.money += 10000

        elif tile.interaction == 'Spectator':
            pass

        elif tile.interaction == 'CashPrize':
            player.money += 5000

        # Keep player at the same position for 2 turns
        elif tile.interaction == 'Defect':
            if player.defect_turn == 0:
                player.defect_turn = 2

    # Draw all elements for the pause menu
    def screen_pause(self):
        event_handler.mode = 'wait'

        # Draw elements
        self.screen.fill((255, 100, 0))
        for element in self.elements_pause:
            element.draw()

    # Load and draw all elements for the winning screen
    def screen_winner(self):
        event_handler.mode = 'wait'

        # Load winning screen elements
        if self.elements_won == None:
            self.elements_won = [
                Text("You win!", 50, (255,255,255), ('center', 230)),
                Text("Congratulations to player " + self.winning_player.color, 25, (255,255,255), ('center', 350)),
                Text("This player won with " + str(self.winning_player.money) + "$", 25, (255,255,255), ('center', 368)),
                Image("buttons/Menu.png",  'Won', ('center', 400)).hover("buttons/Menu_Active.png").click(None, app_state.menu)
            ]

            app_state.next()

        # Draw winning screen
        self.screen.fill((255, 100, 0))
        for element in self.elements_won:
            element.draw()

    def update(self):
        # Run game continuously
        self.event_handler.mode = 'get'

        player = self.get_active_player()

        # Check if player has to skip this turn
        if player.defect_turn >= 1:
            # Skippung turn
            print("Skipping: " + player.color + " turn")

            player.defect_turn -= 1
            self.next_turn()
            
            return

        # Rolling the dice
        if self.turn_state['state'] == 'Dice':

            if player.isRealPlayer:
                if self.turn_state['dice_rolled_tickstart'] > 0:
                    self.entities['dice'].roll()
            else:
                if self.turn_state['dice_rolled_tickstart'] == 0:
                    self.turn_state['dice_rolled_tickstart'] = pygame.time.get_ticks()
                self.entities['dice'].roll()
        
            # Set new pawn position
            if self.turn_state['dice_rolled_tickstart'] > 0 and pygame.time.get_ticks() - self.turn_state['dice_rolled_tickstart'] > self.settings['dice_roll_duration']:
                self.turn_state['dice_score'] = self.entities['dice'].number
                self.turn_state['state'] = 'MovePawn'
                self.turn_state['player_start_position'] = player.position

        # Pawn moving animation
        elif self.turn_state['state'] == 'MovePawn':
        
            if self.turn_state['steps_taken_tickstart'] == 0:
                player.calculate_salary() # Calculate one time
                self.turn_state['steps_taken_tickstart'] = pygame.time.get_ticks()

            if self.turn_state['steps_taken'] < self.turn_state['dice_score']:
                if pygame.time.get_ticks() - self.turn_state['steps_taken_tickstart'] > self.settings['pawn_speed'] * self.turn_state['steps_taken']:
                    self.turn_state['steps_taken'] = self.turn_state['steps_taken'] + 1
                    if player.position < 39:
                        player.position = player.position + 1
                    else:
                        player.position = 0
            else:
                self.turn_state['state'] = 'Interaction'
        
        elif self.turn_state['state'] == 'Interaction':

            if self.turn_state['interaction'] == False:
                self.turn_state['interaction'] = True

                if player.position < self.turn_state['player_start_position']:
                    player.money += 10000 # Went past start
                    
                self.tile_trigger(self.tiles[player.position])

            elif pygame.time.get_ticks() - self.turn_state['interaction_tickstart'] > self.settings['interaction_duration']:
                self.turn_state['state'] = 'EndTurn'

        # Go to the next turn
        if self.turn_state['state'] == 'EndTurn':

            if self.turn_state['endturn_tickstart'] == 0:
                self.turn_state['endturn_tickstart'] = pygame.time.get_ticks()

            if pygame.time.get_ticks() - self.turn_state['endturn_tickstart'] > self.settings['endturn_duration']:
                self.next_turn()

        # Check if there is a winner
        if(player.money >= 100000):
            self.winning_player = player
            app_state.screen_winner()
            return

    # Draw all elements
    def draw(self):
        self.entities['board'].draw()
        self.entities['dice'].draw()
        self.entities['buttons']['help_button'].draw()

        # Reposition players
        for player in self.entities['players']:
            player.draw(self.tiles[player.position].position)
        
        # Draw roll dice button
        if self.get_active_player().isRealPlayer and self.turn_state['dice_rolled_tickstart'] == False:
            self.entities['buttons']['button_roll_dice'].draw()

        # Show buy and skip buttons
        if self.turn_state['state'] == "BuyAttraction":
            self.entities['buttons']['buy'].draw()
            self.entities['buttons']['skip'].draw()

            # Show attraction pricing
            for label in self.turn_state['interaction'].labels:
                label.draw()

        # Show game rules
        if app_state.show_rules:
            self.entities['game_rules'].draw()

        # Show random card
        if self.turn_state['state'] == 'Interaction' and self.turn_state['show_card'] != 0:
            self.turn_state['show_card'].draw()

        # Debug to adjust pawn position
        # for tile in self.tiles:
        #     Image("pieces/orange/piece.png", 'Game', (tile.position.X, tile.position.Y)).draw()
