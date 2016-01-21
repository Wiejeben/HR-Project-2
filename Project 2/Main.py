import pygame

from Library.Image import *
from Init import *
from Library.EventHandler import *
from AppState import *
from Game import *
from Menu import *

# Screen title
pygame.display.set_caption("Groep 3: Buy a Ride")

def Main():
    # Create initial game instance
    app = AppState()
    menu = Menu(app)
    game = Game(4)

    # Event loop
    while True:
        # Background white
        pygame.display.get_surface().fill((255, 255, 255))

        if app.state == "Menu":
            menu.index()

        elif app.state == "Rules":
            menu.rules()

        elif app.state == "Options":
            menu.options()

        elif app.state == "Game":
            if app.paused:  
                game.pause()
            else:
                game.run()
        event_handler.begin()
        event_handler.end()

Main()