import pygame
from time import sleep
from Entities import *
from Player import *
from Library.Image import *
from Library.Text import *

class Game:
    def __init__(self, human_players):
        self.screen = pygame.display.get_surface()
        self.loaded = False

        self.tiles = [
            GameTile(Vector2D(620,630), 'Start'), 
            GameTile(Vector2D(565,630), 'Rollercoasters'), 
            GameTile(Vector2D(510,630), 'WaterRides'), 
            GameTile(Vector2D(455,630), 'QuestionMark'),
            GameTile(Vector2D(410,630), 'ShopsAndStalls'), 

            GameTile(Vector2D(355,630), 'CashFine'), 
            GameTile(Vector2D(270,630), 'TransportRides'), 
            GameTile(Vector2D(210,630), 'QuestionMark'),
            GameTile(Vector2D(150,630), 'ThrillRides'), 
            GameTile(Vector2D(150,630), 'GentleRides'), 

            GameTile(Vector2D(60,630), 'Spectator'), 
            GameTile(Vector2D(60,610), 'TransportRides'),
            GameTile(Vector2D(60,550), 'GentleRides'), 
            GameTile(Vector2D(60,490), 'QuestionMark'), 
            GameTile(Vector2D(60,430), 'Rollercoasters'), 

            GameTile(Vector2D(60,370), 'CashFine'),
            GameTile(Vector2D(60,310), 'ThrillRides'), 
            GameTile(Vector2D(60,250), 'QuestionMark'), 
            GameTile(Vector2D(60,190), 'ShopsAndStalls'), 
            GameTile(Vector2D(60,130), 'WaterRides'),

            GameTile(Vector2D(60,60), 'CashPrize'), 
            GameTile(Vector2D(140,60), 'WaterRides'), 
            GameTile(Vector2D(210,60), 'ThrillRides'), 
            GameTile(Vector2D(270,60), 'QuestionMark'),
            GameTile(Vector2D(330,60), 'GentleRides'),

            GameTile(Vector2D(390,60), 'CashFine'), 
            GameTile(Vector2D(450,60), 'ShopsAndStalls'), 
            GameTile(Vector2D(510,60), 'QuestionMark'), 
            GameTile(Vector2D(570,60), 'Rollercoasters'),
            GameTile(Vector2D(630,60), 'GentleRides'),

            GameTile(Vector2D(710,60), ''), 
            GameTile(Vector2D(710,130), ''), 
            GameTile(Vector2D(710,190), ''), 
            GameTile(Vector2D(710,250), ''),
            GameTile(Vector2D(710,310), ''),

            GameTile(Vector2D(710,370), ''), 
            GameTile(Vector2D(710,430), ''), 
            GameTile(Vector2D(710,490), ''), 
            GameTile(Vector2D(710,550), ''),
            GameTile(Vector2D(710,610), '')
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


        # REFACTOR APPSTATE > GAME([COLOR PLAYER > REAL PLAYER TRUE / FALSE])
        players = []
        print("Human players: " + str(human_players))
        if human_players > 0:
            players.append(Player(0, False, "green")) # The Player
        else:
            players.append(Player(0, True, "green")) # The Player
            #players.append(Player(0, False, "green")) # AI player
        if human_players > 1:
            players.append(Player(0, False, "blue")) # The Player
        else:
            players.append(Player(0, False, "blue")) # AI player
        if human_players > 2:
            players.append(Player(0, False, "red")) # The Player
        else:
            players.append(Player(0, False, "red")) # AI player
        if human_players > 3:
            players.append(Player(0, False, "yellow")) # The Player
        else:
            players.append(Player(0, False, "yellow")) # AI player

        self.settings = {
            'pawn_speed' : 15,
            'dice_roll_duration' : 15
        }

        self.elements_pause = [
            Text("Pause menu", 50, (100, 10, 10), ('center', 10)),

            Image("buttons/Menu.png",  'Pause', ('center', 300)).hover("buttons/Menu_Active.png").click(None, app_state.menu),
            Image("buttons/Resume.png",  'Pause', ('center', 400)).hover("buttons/Resume_Active.png").click(None, app_state.pause),
            Image("buttons/Exit.png", 'Pause', ('center', 500)).hover("buttons/Exit_Active.png").click(None, app_state.exit)
        ]

        self.entities = {
            'board': Image("board/game_board.png", 'Game', (0,0), (700,700)),
            'players': players,
            'dice': Dice(Vector2D(850,350), Vector2D(64, 64)),
            'buttons' : {
                'button_roll_dice' : Image("buttons/Roll.png", 'Game', (750,450)).hover("buttons/Roll_Active.png").click(None, self.dice_click),
            },
            'text_labels' :{
               'turn_label' : Text("Current turn: ", 20, (0, 0, 0), (750, 50)),
               'money_label' : Text("$ 0", 20, (0, 90, 0), (750, 75)),
            }
        }

        self.turn_state = {
            'active_player_id'      : 0,
            'state'                 : 'Dice',
            'dice_rolled_tickstart' : 0,
            'dice_score'            : 0,
            'steps_taken'           : 0,
            'steps_taken_tickstart' : 0,
            'start_position'        : 0
        }

    def getActivePlayer(self):
        return self.entities['players'][self.turn_state['active_player_id']]

    def nextTurn(self):
        self.turn_state = {
            'active_player_id'      : (self.turn_state['active_player_id'] + 1) % len(self.entities['players']),
            'state'                 : 'Dice',
            'dice_rolled_tickstart' : 0,
            'dice_score'            : 0,
            'steps_taken'           : 0,
            'steps_taken_tickstart' : 0,
            'player_start_position' : 0
        }

    def dice_click(self):
        self.turn_state['dice_rolled_tickstart'] = pygame.time.get_ticks()

    def update(self):
        # Set application mode to continuously run
        global event_handler, app_state
        event_handler.mode = 'get'

        # Get the player who's turn it is
        player = self.getActivePlayer()

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
        
        if self.turn_state['state'] == 'MovePawn':
            
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
        if self.turn_state['state'] == 'Interaction':

            # Give the player 20k when landing on start, give 10k when passing start
            if player.position == 0:
                player.money += 20000
            elif player.position < self.turn_state['player_start_position']:
                player.money += 10000
            
            # TODO : Choose attraction
            self.tile_interact(self.tiles[player.position].interaction)

            self.nextTurn() 

        self.draw()

    def draw(self):
        self.entities['board'].draw()
        
        for player in self.entities['players']:
            player.draw(self.tiles[player.position].position)
        
        if self.getActivePlayer().isRealPlayer and self.turn_state['dice_rolled_tickstart'] == False:
            self.entities['buttons']['button_roll_dice'].draw()

        self.entities['text_labels']['turn_label'].set_text(self.getActivePlayer().color + '\'s turn' )
        self.entities['text_labels']['money_label'].set_text('$ ' + str(self.getActivePlayer().money))
        self.entities['text_labels']['turn_label'].draw()
        self.entities['text_labels']['money_label'].draw()

        self.getActivePlayer().board.draw()

        self.entities['dice'].draw()

    def tile_interact(self, interaction):
        player = self.getActivePlayer()
        if interaction == 'ThrillRides':
            print ("ThrillRides")
            player.buy_attraction(self.attractions[0], 0)

        elif interaction == 'ShopsAndStalls':
            print ("ShopsAndStalls")
            player.buy_attraction(self.attractions[3], 1)
            pass
        elif interaction == 'TransportRides':
            print ("TransportRides")
            player.buy_attraction(self.attractions[6], 2)
            pass
        elif interaction == 'WaterRides':
            player.buy_attraction(self.attractions[19], 3)
            pass
        elif interaction == 'GentleRides':
            print ("GentleRides")
            player.buy_attraction(self.attractions[16], 4)
            pass
        elif interaction == 'Rollercoasters':
            print ("Rollercoasters")
            player.buy_attraction(self.attractions[15], 5)
            pass
        elif interaction == 'QuestionMark':
            print ("QuestionMark")
            pass
        elif interaction == 'CashFine':
            pass
        elif interaction == 'Start':
            pass
        elif interaction == 'Spectator':
            pass
        elif interaction == 'CashPrize':
            pass
        elif interaction == 'Defect':
            pass

    def pause(self):
        event_handler.mode = 'wait'
        self.screen.fill((255, 100, 0))

        # Draw elements
        for element in self.elements_pause:
            element.draw()

