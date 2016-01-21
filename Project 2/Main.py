import pygame

from time import sleep
from pygame.locals import *

from UIToolKit.Image import *
from Init import *
from UIToolKit.EventHandler import *
from AppState import *
#from Game import *
from Menu import *


# Colors
white = 255, 255, 255
green = 50, 255, 100
yellow = 255, 255, 0
orange = 255, 100, 0

pygame.display.set_caption("Groep 3: Buy a Ride")


def Main():
    # Create initial game instance
    app = AppState()
    menu = Menu(app)
    #game = Game(4)
    

    # Event loop
    while True:
        event_handler.event()

        if app.state == "Menu":
            menu.draw()

        pygame.display.flip()

Main()