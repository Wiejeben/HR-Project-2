import pygame
from time import sleep
from Entities import *
from UIToolKit.Button import *
from UIToolKit.ImageUtils import *
from Player import *
from Node import *

class Game:
    def __init__(self, background, amount_opponents):
        self.background = background
        self.loaded = False
        
        self.board = GameBoard(Vector2D(0,0), Vector2D(768,768))
        self.dice = Dice(Vector2D(850,350), Vector2D(64, 64))
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

        # Buttons uitoolkit?
        self.ButtonList = []

        self.active_player_id = 0
        self.players = []
        self.players.append(Player(0, True, "blue", 0)) # The Player

        self.players.append(Player(0, False, "red", 1)) # AI player
        self.players.append(Player(0, False, "green", 2)) # AI player
        self.players.append(Player(0, False, "yellow", 3)) # AI player
        for player in self.players:
            player.position = 1

    def load(self):
        yellow = 255, 255, 0
        self.background.fill(yellow)
        font = pygame.font.Font(None, 36)
        text = font.render("Game", 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = self.background.get_rect().centerx
        self.background.blit(text, textpos)

    def getActivePlayer(self):
        return self.players[self.active_player_id]

    def nextTurn(self):
        self.players[self.active_player_id].turn_state = 0
        self.active_player_id = (self.active_player_id + 1) % len(self.players)
    
        
    # ???
    def playerRolledDice():
        #self.players[self.active_player_id].turn_state = 1
        for i in range(1,10):
            self.dice.roll()
            self.draw(screen)
            pygame.time.delay(500)
            

    def run(self, screen):

        # Get the player who's turn it is
        player = self.getActivePlayer()
        if player.isRealPlayer: #and player.turn_state == 0:
            #player.turn_state = 1
            # ????
            #diceButton = Button(ImageUtils.Screen.get_width() / 2 - 100, 200, 200, 100, "normal_example.png", "hover_example.png", "pressed_example.png", self.playerRolledDice)
            #self.ButtonList.append(diceButton)
            self.dice.roll()
            self.draw(screen)
        else:
            for i in range(1,10):
                self.dice.roll()
                self.draw(screen)
                pygame.time.delay(50)
               
        for i in range(0, self.dice.number):
            if player.position < 39:
                player.position = player.position + 1
            else:
                player.position = 0
            self.draw(screen)
            sleep(0.2)


        self.nextTurn()

    def draw(self, screen):
        self.board.render(screen)
        self.dice.render(screen)
        for player in self.players:
            player.drawPawn(screen, self.tiles[player.position].position)
        player = self.getActivePlayer()

        screen.blit(pygame.transform.scale(player.texture, (player.size.X, player.size.Y)), (840 , 150))

        pygame.display.flip()

    def pause(self):
        print("Paused")
        orange = 255, 100, 0 
        self.background.fill(orange)
        font = pygame.font.Font(None, 36)
        text = font.render("Paused!", 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = self.background.get_rect().centerx
        self.background.blit(text, textpos)

    def handleInputs(self, event):
        for button in self.ButtonList:
            button.handleInputEvents(event)

