﻿import pygame
from time import sleep
from Entities import *
from Player import *
from Library.Image import *
from Library.Text import *

class Game:
    def __init__(self, human_players):
        self.screen = pygame.display.get_surface()
        self.loaded = False

        bottom_y = 600
        left_x = 5
        top_y = 5
        right_x = 667

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

        self.attractions = {
            'ThrillRides' : { # NOT COMPLETE
                '3D Cinema' : Attraction('3D Cinema', 10000),
                'Train' : Attraction('Train', 10000),
            },
            'WaterRides' : { # NOT COMPLETE
                'Boat Hire' : Attraction('Boat Hire', 3000),
            },
            'TransportRides' : {
                'Train' : Attraction('Train', 5000),
                'Monorail' : Attraction('Monorail', 12000),
                'Chairlift' : Attraction('Chairlift', 8000),
            },
            'GentleRides' : {
                'Haunted House' : Attraction('Haunted House', 3500),
                'Ferriswheel' : Attraction('Ferriswheel', 6000),
                'Merrie-go-round' : Attraction('Merrie-go-round', 3000),
                'Maze' : Attraction('Maze', 7500),
                'Dodgems' : Attraction('Dodgems', 7000),
                'Monster Trucks' : Attraction('Monster Trucks', 10000),
                'Racing Cars' : Attraction('Racing Cars', 11000),
                'Circus' : Attraction('Circus', 4000),
                'Minigold' : Attraction('Minigold', 8000),
                'Observation Tower' : Attraction('Observation Tower', 15000),
                'Spiral Slide' : Attraction('Spiral Slide', 2500),
            },
            'ShopsAndStalls' : { # NOT COMPLETE
                'Balloon Stall' : Attraction('Balloon Stall', 1900),
            },
            'Rollercoasters' : {
                'Bobsleigh Coaster' : Attraction('Bobsleigh Coaster', 18000),
                'Corkscrew Rollercoaster' : Attraction('Corkscrew Rollercoaster', 25000),
                'Giga Coaster' : Attraction('Giga Coaster', 27000),
                'Junior Rollercoaster' : Attraction('Junior Rollercoaster', 7500),
                'Looping Rollercoaster' : Attraction('Looping Rollercoaster', 20000),
                'Mine Train Coaster' : Attraction('Mine Train Coaster', 12500),
                'Stand-up Rollercoaster' : Attraction('Stand-up Rollercoaster', 19000),
                'Steel Twister Rollercoaster' : Attraction('Steel Twister Rollercoaster', 30000),
                'Wild Mouse' : Attraction('Wild Mouse', 6500),
                'Wooden Rollercoaster' : Attraction('Wooden Rollercoaster', 10000),
            }
        }

        players = []
        print("Human players: " + str(human_players))
        if human_players > 0:
            players.append(Player(0, True, "green")) # The Player
        else:
            players.append(Player(0, False, "green")) # AI player
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
            'pawn_speed' : 500,
            'dice_roll_duration' : 500
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

    
    def tile_interact(self, interaction):
        player = self.getActivePlayer()
        if interaction == 'ThrillRides':
            print ("ThrillRides")
            player.board.attractions.append(self.attractions['ThrillRides']['Train'])

        elif interaction == 'ShopsAndStalls':
            print ("ShopsAndStalls")
            player.board.attractions.append(self.attractions['ShopsAndStalls']['Balloon Stall'])
            pass
        elif interaction == 'TransportRides':
            print ("TransportRides")
            player.board.attractions.append(self.attractions['TransportRides']['Train'])
            pass
        elif interaction == 'WaterRides':
            print ("WaterRides")
            player.board.attractions.append(self.attractions['WaterRides']['Boat Hire'])
            pass
        elif interaction == 'GentleRides':
            print ("GentleRides")
            pass
        elif interaction == 'Rollercoasters':
            print ("Rollercoasters")
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

    def update(self):
        # Set application mode to continuously run
        global event_handler, app_state
        event_handler.mode = 'get'

        # Get the player who's turn it is
        player = self.getActivePlayer()

        if self.turn_state['dice_rolled_finished'] == False:
            # BELOW IS RAN WHEN DICE HAS TO BE ROLLED

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
            # BELOW IS RAN WHEN DICE ROLL IS FINISHED
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
                # BELLOW IS RAN WHEN THE PAWN HAS FINISHED MOVING
                self.tile_interact(self.tiles[player.position].interaction)


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

        # Debug to adjust pawn position
        if True == False:
            for tile in self.tiles:
                Image("pieces/red/piece.png", 'Game', (tile.position.X, tile.position.Y)).draw()

    def pause(self):
        event_handler.mode = 'wait'
        self.screen.fill((255, 100, 0))

        # Draw elements
        for element in self.elements_pause:
            element.draw()

