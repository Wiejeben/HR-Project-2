import pygame
from sys import exit

class AppState:
    def __init__(self):
        self.state = "Menu"
        self.paused = False

    def menu(self):
        self.state = "Menu"

    def rules(self):
        self.state = "Rules"

    def options(self):
        self.state = "Options"

    # Close game
    def exit(self):
        exit()
    
    # Get inside game
    def start(self):
        self.state = "Game"

    # Interrupt gameplay
    def togglePause(self):
        print("Toggle pause")
        if self.state == "Game":

            if self.paused:
                self.paused = False
            else:
                self.paused = True
    
    # Resume gameplay
    def resume(self):
        self.paused = False