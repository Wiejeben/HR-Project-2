import pygame
from Library.Image import *
from Init import *

class AppState:
    def __init__(self):
        self.state = "Menu"
        self.show_rules = False
        self.temp_state = None
        self.player_amount = []

    def set_state(self, state):
        self.temp_state = state

    def switch_state(self):
        if self.temp_state != None:
            self.state = self.temp_state
            self.temp_state = None
    
    def game_rules(self):
        if self.show_rules:
            self.show_rules = False
        else:
            self.show_rules = True

    def menu(self):
        self.set_state("Menu")
        self.next()

    def rules(self):
        self.set_state("Rules")
        self.next()

    def options(self):
        self.set_state("Options")
        self.next()

    def player_select(self):
        self.set_state("PlayerSelect")
        self.next()

    # Go to next frame
    def next(self):
        pygame.event.post(pygame.event.Event(pygame.locals.USEREVENT))

    # Close game
    def exit(self):
        exit()
    
    # Get inside game
    def start(self, player_amount):
        self.player_amount = player_amount
        self.set_state("GameStart")
        self.next()

    def pause(self):
        if self.state == "Game":
            self.set_state("Pause")
            print('pause app state')

        if self.state == "Pause":
            self.set_state("Game")

        self.next()
    
    # Resume gameplay
    def resume(self):
        self.paused = False