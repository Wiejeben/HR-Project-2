import pygame
from time import sleep
from Entities import *
from Player import *
from Library.Image import *
from Library.Text import *

class Game:
    def __init__(self, human_players):
        self.screen = pygame.display.get_surface()

        # Initialize music
        pygame.mixer.music.load("Content/sounds/Track1.wav")
        pygame.mixer.music.play(-1, 0.0)

        # Some temp tile positions
        bottom_y = 600
        left_x = 5
        top_y = 5
        right_x = 667

        # Board tiles
        self.tiles = [
            # Bottom
            GameTile(Vector2D(640,bottom_y), 'Start'), 
            GameTile(Vector2D(558,bottom_y), 'Rollercoasters'), 
            GameTile(Vector2D(503,bottom_y), 'WaterRides'),
            GameTile(Vector2D(448,bottom_y), 'QuestionMark'),
            GameTile(Vector2D(393,bottom_y), 'ShopsAndStalls'),
            GameTile(Vector2D(338,bottom_y), 'CashFine'),
            GameTile(Vector2D(283,bottom_y), 'TransportRides'),
            GameTile(Vector2D(228,bottom_y), 'QuestionMark'),
            GameTile(Vector2D(173,bottom_y), 'ThrillRides'),
            GameTile(Vector2D(118,bottom_y), 'GentleRides'),
            GameTile(Vector2D(35,bottom_y), 'Spectator'),

            # Left
            GameTile(Vector2D(left_x,542), 'TransportRides'),
            GameTile(Vector2D(left_x,488), 'GentleRides'), 
            GameTile(Vector2D(left_x,434), 'QuestionMark'), 
            GameTile(Vector2D(left_x,379), 'Rollercoasters'), 
            GameTile(Vector2D(left_x,323), 'CashFine'),
            GameTile(Vector2D(left_x,268), 'ThrillRides'), 
            GameTile(Vector2D(left_x,214), 'QuestionMark'), 
            GameTile(Vector2D(left_x,159), 'ShopsAndStalls'), 
            GameTile(Vector2D(left_x,105), 'WaterRides'),

            # Top
            GameTile(Vector2D(35,top_y), 'CashPrize'), 
            GameTile(Vector2D(118,top_y), 'WaterRides'), 
            GameTile(Vector2D(173,top_y), 'ThrillRides'), 
            GameTile(Vector2D(228,top_y), 'QuestionMark'),
            GameTile(Vector2D(283,top_y), 'GentleRides'),
            GameTile(Vector2D(338,top_y), 'CashFine'), 
            GameTile(Vector2D(393,top_y), 'ShopsAndStalls'), 
            GameTile(Vector2D(448,top_y), 'QuestionMark'), 
            GameTile(Vector2D(503,top_y), 'Rollercoasters'),
            GameTile(Vector2D(558,top_y), 'GentleRides'),
            GameTile(Vector2D(640,top_y), 'Defect'),

            # Right
            GameTile(Vector2D(right_x,105), 'ShopsAndStalls'), 
            GameTile(Vector2D(right_x,159), 'WaterRides'), 
            GameTile(Vector2D(right_x,214), 'QuestionMark'),
            GameTile(Vector2D(right_x,268), 'ThrillRides'),
            GameTile(Vector2D(right_x,323), 'CashFine'), 
            GameTile(Vector2D(right_x,379), 'Rollercoasters'), 
            GameTile(Vector2D(right_x,434), 'QuestionMark'), 
            GameTile(Vector2D(right_x,488), 'GentleRides'),
            GameTile(Vector2D(right_x,542), 'ThrillRides')
        ]

        self.chance_cards = [
            #ChanceCard('cards/card01.png', -5000),
            #ChanceCard('cards/card02.png', -6000),
            #ChanceCard('cards/card03.png', -10000),
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

        self.attractions = [
            Attraction('3D Cinema', 10000, 'thrill_rides'),

            Attraction('Boat Hire', 3000, 'water_rides'),

            Attraction('Train', 5000, 'transport_rides'),
            Attraction('Monorail', 12000, 'transport_rides'),
            Attraction('Chairlift', 8000, 'transport_rides'),

            Attraction('Haunted House', 3500, 'gentle_rides'),
            Attraction('Ferriswheel', 6000, 'gentle_rides'),
            Attraction('Merrie-go-round', 3000, 'gentle_rides'),
            Attraction('Maze', 7500, 'gentle_rides'),
            Attraction('Dodgems', 7000, 'gentle_rides'),
            Attraction('Monster Trucks', 10000, 'gentle_rides'),
            Attraction('Racing Cars', 11000, 'gentle_rides'),
            Attraction('Circus', 4000, 'gentle_rides'),
            Attraction('Minigold', 8000, 'gentle_rides'),
            Attraction('Observation Tower', 15000, 'gentle_rides'),
            Attraction('Spiral Slide', 2500, 'gentle_rides'),

            Attraction('Bobsleigh Coaster', 18000, 'rollercoaster'),
            Attraction('Corkscrew Rollercoaster', 25000, 'rollercoaster'),
            Attraction('Giga Coaster', 27000, 'rollercoaster'),
            Attraction('Junior Rollercoaster', 7500, 'rollercoaster'),
            Attraction('Looping Rollercoaster', 20000, 'rollercoaster'),
            Attraction('Mine Train Coaster', 12500, 'rollercoaster'),
            Attraction('Stand-up Rollercoaster', 19000, 'rollercoaster'),
            Attraction('Steel Twister Rollercoaster', 30000, 'rollercoaster'),
            Attraction('Wild Mouse', 6500, 'rollercoaster'),
            Attraction('Wooden Rollercoaster', 10000, 'rollercoaster'),

            Attraction('Balloon Stall', 1900, 'shops_and_stalls'),
        ]

        players = []
        # Load players
        for i, isRealPlayer in enumerate(human_players, start=0):
            player = Player(isRealPlayer, i)

            # Set first player to be active
            if i == 0:
                player.isActive = True

            players.append(player)

        self.settings = {
            'pawn_speed' : 150,
            'dice_roll_duration' : 1500,
            'interaction_duration' : 2500,
            'endturn_duration' : 1000
        }

        self.elements_pause = [
            Text("Pause menu", 50, (255, 255, 255), ('center', 230)),

            Image("buttons/Resume.png",  'Pause', ('center', 300)).hover("buttons/Resume_Active.png").click(None, app_state.pause),
            Image("buttons/Menu.png",  'Pause', ('center', 400)).hover("buttons/Menu_Active.png").click(None, app_state.menu),
            Image("buttons/Exit.png", 'Pause', ('center', 500)).hover("buttons/Exit_Active.png").click(None, app_state.exit)
        ]

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

        # Current turn perferences
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

    def getActivePlayer(self):
        for player in self.entities['players']:
            if player.isActive:
                return player

    def nextTurn(self):
        # Reset turn perferences
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

    def update(self):
        # Set application mode to continuously run
        global event_handler, app_state
        event_handler.mode = 'get'

        player = self.getActivePlayer()
        
        # If skipping a turn
        if player.defect_turn >= 1:
            # Skippung turn
            print("Skipping: " + player.color + " turn")
            player.defect_turn -= 1
            self.nextTurn()
        else:
            # Rolling the dice
            if self.turn_state['state'] == 'Dice':

                if not player.isRealPlayer: # IF AI
                    if self.turn_state['dice_rolled_tickstart'] == 0:
                        self.turn_state['dice_rolled_tickstart'] = pygame.time.get_ticks()
                    self.entities['dice'].roll()

                if player.isRealPlayer:
                    if self.turn_state['dice_rolled_tickstart'] > 0:
                        self.entities['dice'].roll()
            
                if self.turn_state['dice_rolled_tickstart'] > 0 and pygame.time.get_ticks() - self.turn_state['dice_rolled_tickstart'] > self.settings['dice_roll_duration']:
                    self.turn_state['dice_score'] = self.entities['dice'].number
                    self.turn_state['state'] = 'MovePawn'
                    self.turn_state['player_start_position'] = player.position
        
            # Buying an attraction
            elif self.turn_state['state'] == 'BuyAttraction':
                pass

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
            
            # NOTE : Michael what does this exactly?
            elif self.turn_state['state'] == 'Interaction':
  
                # TODO : Choose attraction
                if self.turn_state['interaction'] == False:
                    self.turn_state['interaction'] = True
                    if player.position < self.turn_state['player_start_position']:
                        player.money += 10000 # Went past start
                    self.tile_interact(self.tiles[player.position].interaction)

                elif pygame.time.get_ticks() - self.turn_state['interaction_tickstart'] > self.settings['interaction_duration']:
                    self.turn_state['state'] = 'EndTurn'

            # Go to the next turn
            if self.turn_state['state'] == 'EndTurn':

                if self.turn_state['endturn_tickstart'] == 0:
                    self.turn_state['endturn_tickstart'] = pygame.time.get_ticks()

                if pygame.time.get_ticks() - self.turn_state['endturn_tickstart'] > self.settings['endturn_duration']:
                    self.nextTurn()

    def draw(self):
        self.entities['board'].draw()
        
        # Reposition players
        for player in self.entities['players']:
            player.draw(self.tiles[player.position].position)
        
        if self.getActivePlayer().isRealPlayer and self.turn_state['dice_rolled_tickstart'] == False:
            self.entities['buttons']['button_roll_dice'].draw()

        self.entities['dice'].draw()

        # show buy and skip buttons
        if self.turn_state['state'] == "BuyAttraction":
            self.entities['buttons']['buy'].draw()
            self.entities['buttons']['skip'].draw()

            Text(str(self.turn_state['interaction'].price) + "$", 25, (255,255,255), (75, 725)).draw()

        self.entities['buttons']['help_button'].draw()
        # show game rules
        if app_state.show_rules:
            self.entities['game_rules'].draw()

        if self.turn_state['state'] == 'Interaction' and self.turn_state['show_card'] != 0:
            self.turn_state['show_card'].draw()

        # Debug to adjust pawn position
        if True == False:
            for tile in self.tiles:
                Image("pieces/red/piece.png", 'Game', (tile.position.X, tile.position.Y)).draw()

    def attraction_skip(self):
        if self.turn_state['state'] == "BuyAttraction":
            # Reset click action
            self.entities['buttons']['buy'].click()
            self.turn_state['state'] = 'EndTurn'

    def attraction_buy_confirmed(self, position):
        if self.turn_state['state'] == "BuyAttraction":
            self.getActivePlayer().attraction_buy(self.turn_state['interaction'], position)
            self.attraction_skip()

    def attraction_buy(self, attraction, position):
        player = self.getActivePlayer()

        # First see if player has enough money
        if player.money > attraction.price:
            # Store attraction that we are trying to buy
            self.turn_state['state'] = "BuyAttraction"
            self.turn_state['interaction'] = attraction

            if not player.isRealPlayer: # IF AI
                # 80% odds that the AI is going to buy
                if random.randint(0,10) < 8:
                    print("Buy attraction")
                    self.attraction_buy_confirmed(position)
                else:
                    print("Skip attraction")
                    self.attraction_skip()
            else:
                # Setup buy click event
                self.entities['buttons']['buy'].click(None, self.attraction_buy_confirmed, position)

    def attraction_event(self, id, position):
        attraction = self.attractions[id]

        if attraction.owner == None:
            # Buy attraction
            self.attraction_buy(attraction,position)
        else:
            print("Owned by " + attraction.owner.color)

    def tile_interact(self, interaction):
        player = self.getActivePlayer()
        
        #Debug
        print(interaction)

        if interaction == 'ThrillRides':
            self.attraction_event(0,0)

        elif interaction == 'ShopsAndStalls':
            self.attraction_event(3,1)

        elif interaction == 'TransportRides':
            self.attraction_event(6,2)

        elif interaction == 'WaterRides':
            self.attraction_event(19,3)

        elif interaction == 'GentleRides':
            self.attraction_event(16,4)

        elif interaction == 'Rollercoasters':
            self.attraction_event(15,5)

        elif interaction == 'QuestionMark':
            self.turn_state['show_card'] = random.choice(self.chance_cards)
            player.money += self.turn_state['show_card'].money
            self.turn_state['interaction_tickstart'] = pygame.time.get_ticks()

        elif interaction == 'CashFine':
            player.calculate_player_class()

            if player.player_class >= 2:
                print("Fined player money")
                player.money = player.money - 5000

        elif interaction == 'Start':
            player.money += 10000
        elif interaction == 'Spectator':
            pass

        elif interaction == 'CashPrize':
            player.money += 5000

        elif interaction == 'Defect':
            if player.defect_turn == 0:
                player.defect_turn = 2

    def pause(self):
        event_handler.mode = 'wait'
        self.screen.fill((255, 100, 0))

        # Draw elements
        for element in self.elements_pause:
            element.draw()
