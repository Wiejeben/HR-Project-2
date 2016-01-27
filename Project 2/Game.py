import pygame
from time import sleep
from Entities import *
from Player import *
from Library.Image import *
from Library.Text import *

class Game:
    def __init__(self, amount_opponents):
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

        self.attractions = {
            'ThrillRides' : {
                
            },
            'WaterRides' : {
                
            },
            'TransportRides' : {
                Attraction('Train', 5000),
                Attraction('Monorail', 12000),
                Attraction('Chairlift', 8000),
            },
            'GentleRides' : {
                Attraction('Haunted House', 3500),
                Attraction('Ferriswheel', 6000),
                Attraction('Merrie-go-round', 3000),
                Attraction('Maze', 7500),
                Attraction('Dodgems', 7000),
                Attraction('Monster Trucks', 10000),
                Attraction('Racing Cars', 11000),
                Attraction('Circus', 4000),
                Attraction('Minigold', 8000),
                Attraction('Observation Tower', 15000),
                Attraction('Spiral Slide', 2500),
            },
            'ShopsAndStalls' : {
                
            },
            'Rollercoasters' : {
                Attraction('Bobsleigh Coaster', 18000),
                Attraction('Corkscrew Rollercoaster', 25000),
                Attraction('Giga Coaster', 27000),
                Attraction('Junior Rollercoaster', 7500),
                Attraction('Looping Rollercoaster', 20000),
                Attraction('Mine Train Coaster', 12500),
                Attraction('Stand-up Rollercoaster', 19000),
                Attraction('Steel Twister Rollercoaster', 30000),
                Attraction('Wild Mouse', 6500),
                Attraction('Wooden Rollercoaster', 10000),
            }
        }

        players = []
        players.append(Player(0, False, "blue")) # The Player
        players.append(Player(0, False, "red")) # AI player
        players.append(Player(0, True, "green")) # AI player
        players.append(Player(0, False, "yellow")) # AI player

        self.settings = {
            'pawn_speed' : 500,
            'dice_roll_duration' : 500
        }

        self.entities = {
            'board': Image("board/game_board.png", 'Game', (0,0), (700,700)),
            'players': players,
            'dice': Dice(Vector2D(850,350), Vector2D(64, 64)),
            'buttons' : {
                'button_roll_dice' : Image("buttons/Start.png", 'Game', (750,450)).hover("buttons/Start_Active.png").click(None, self.dice_click),
            },
        }

        self.turn_state = {
            'active_player_id' : 0,
            'dice_rolled_tickstart' : 0,
            'dice_rolled_finished' : False,
            'dice_score' : 0,
            'steps_taken' : 0,
            'steps_taken_tickstart' : 0
        }


    def getActivePlayer(self):
        return self.entities['players'][self.turn_state['active_player_id']]

    def nextTurn(self):
        self.turn_state = {
            'active_player_id' : (self.turn_state['active_player_id'] + 1) % len(self.entities['players']),
            'dice_rolled_tickstart' : 0,
            'dice_rolled_finished' : False,
            'dice_score' : 0,
            'steps_taken' : 0,
            'steps_taken_tickstart' : 0,
        }

    def dice_click(self):
        self.turn_state['dice_rolled_tickstart'] = pygame.time.get_ticks()

    def update(self):
        # Set application mode to continuously run
        global event_handler, app_state
        event_handler.mode = 'get'

        # Get the player who's turn it is
        player = self.getActivePlayer()

        if self.turn_state['dice_rolled_finished'] == False:


            if not player.isRealPlayer: # IF AI
                if self.turn_state['dice_rolled_tickstart'] == 0:
                    self.turn_state['dice_rolled_tickstart'] = pygame.time.get_ticks()
                self.entities['dice'].roll()
                
            if player.isRealPlayer:
                if self.turn_state['dice_rolled_tickstart'] > 0:
                    self.entities['dice'].roll()

            if self.turn_state['dice_rolled_tickstart'] > 0 and pygame.time.get_ticks() - self.turn_state['dice_rolled_tickstart'] > self.settings['dice_roll_duration']:
                self.turn_state['dice_score'] = self.entities['dice'].number
                self.turn_state['dice_rolled_finished'] = True
        else:

            if self.turn_state['steps_taken_tickstart'] == 0:
                self.turn_state['steps_taken_tickstart'] = pygame.time.get_ticks()

            if self.turn_state['steps_taken'] < self.turn_state['dice_score']:
                if pygame.time.get_ticks() - self.turn_state['steps_taken_tickstart'] > self.settings['pawn_speed'] * self.turn_state['steps_taken']:
                    self.turn_state['steps_taken'] = self.turn_state['steps_taken'] + 1
                    if player.position < 39:
                        player.position = player.position + 1
                    else:
                        player.position = 0
                    
            else:

                

                player.interact(self.tiles[player.position].interaction)


                self.nextTurn() 

        self.draw()

    def draw(self):
        self.entities['board'].draw()
        
        for player in self.entities['players']:
            player.draw(self.tiles[player.position].position)
        
        if self.getActivePlayer().isRealPlayer and self.turn_state['dice_rolled_tickstart'] == False:
            self.entities['buttons']['button_roll_dice'].draw()

        self.getActivePlayer().board.draw()

        self.entities['dice'].draw()

    def pause(self):
        event_handler.mode = 'wait'
        self.screen.fill((255, 100, 0))

        # Draw elements
        for element in self.elements_pause:
            element.draw()

