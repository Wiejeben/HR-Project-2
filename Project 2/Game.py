import pygame
from time import sleep
from Entities import *
from Player import *
from Library.Image import *

class Game:
    def __init__(self, amount_opponents):
        self.screen = pygame.display.get_surface()
        self.loaded = False

        self.tiles = [
            GameTile(Vector2D(710,720)), 
            GameTile(Vector2D(630,720)), 
            GameTile(Vector2D(570,720)), 
            GameTile(Vector2D(510,720)),
            GameTile(Vector2D(450,720)), 

            GameTile(Vector2D(390,720)), 
            GameTile(Vector2D(330,720)), 
            GameTile(Vector2D(270,720)),
            GameTile(Vector2D(210,720)), 
            GameTile(Vector2D(150,720)), 

            GameTile(Vector2D(60,720)), 
            GameTile(Vector2D(60,610)),
            GameTile(Vector2D(60,550)), 
            GameTile(Vector2D(60,490)), 
            GameTile(Vector2D(60,430)), 

            GameTile(Vector2D(60,370)),
            GameTile(Vector2D(60,310)), 
            GameTile(Vector2D(60,250)), 
            GameTile(Vector2D(60,190)), 
            GameTile(Vector2D(60,130)),

            GameTile(Vector2D(60,60)), 
            GameTile(Vector2D(140,60)), 
            GameTile(Vector2D(210,60)), 
            GameTile(Vector2D(270,60)),
            GameTile(Vector2D(330,60)),

            GameTile(Vector2D(390,60)), 
            GameTile(Vector2D(450,60)), 
            GameTile(Vector2D(510,60)), 
            GameTile(Vector2D(570,60)),
            GameTile(Vector2D(630,60)),

            GameTile(Vector2D(710,60)), 
            GameTile(Vector2D(710,130)), 
            GameTile(Vector2D(710,190)), 
            GameTile(Vector2D(710,250)),
            GameTile(Vector2D(710,310)),

            GameTile(Vector2D(710,370)), 
            GameTile(Vector2D(710,430)), 
            GameTile(Vector2D(710,490)), 
            GameTile(Vector2D(710,550)),
            GameTile(Vector2D(710,610))
        ]

       
        self.active_player_id = 0

        players = []
        players.append(Player(0, True, "blue")) # The Player
        players.append(Player(0, False, "red")) # AI player
        players.append(Player(0, False, "green")) # AI player
        players.append(Player(0, False, "yellow")) # AI player

        self.entities = {
            'board': Image("board/game_board.png", 'Game', (160,80), (600,600)),
            'players': players,
            'dice': Dice(Vector2D(850,350), Vector2D(64, 64))
        }

        for player in self.entities['players']:
            player.position = 1

    # DEPRECATED            Game bootstrap (inactive)
    def load(self):
        font = pygame.font.Font(None, 36)
        text = font.render("Game", 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = self.screen.get_rect().centerx
        self.screen.blit(text, textpos)

    def getActivePlayer(self):
        return self.entities['players'][self.active_player_id]

    def nextTurn(self):
        self.active_player_id = (self.active_player_id + 1) % len(self.entities['players'])

    def draw_dice_roll(self):
        for i in range(1,10):
            self.entities['dice'].roll()
            self.draw()
            sleep(0.05)

    def run(self):
        # Set application mode to continuously run
        global event_handler, app_state
        event_handler.mode = 'get'

        
        # Get the player who's turn it is
        player = self.getActivePlayer()
        if player.isRealPlayer:
            # Let the player click on dice roll 
            self.entities['buttons'] = Image("buttons/Start.png", 'Game', ('center', 300)).hover("buttons/Start_Active.png").click(None, self.draw_dice_roll),
        else:
            self.draw_dice_roll()
               
        for i in range(1, self.entities['dice'].number):
            if player.position < 39:
                player.position = player.position + 1
            else:
                player.position = 0
            self.draw()
            sleep(0.2)

            
        self.draw()

        # Move player for the amount rolled
        
        self.nextTurn()

    def draw(self):
        for x in self.entities:
            if type(x) is not list:
                self.entities[x].draw()

            

        #self.board.draw()

        #self.dice.render(self.screen)
        #for player in self.players:
            #player.drawPawn(self.tiles[player.position].position)

        #self.getActivePlayer().drawPawn(Vector2D(840 , 150))

    def pause(self):
        print("Paused")
        orange = 255, 100, 0 
        self.screen.fill(orange)
        font = pygame.font.Font(None, 36)
        text = font.render("Paused!", 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = self.screen.get_rect().centerx
        self.screen.blit(text, textpos)


