import pygame
from Library.Image import *
from Init import *
from Library.EventHandler import *
from Library.AppState import *
from Game import *
from Menu import *

# Screen title
pygame.display.set_caption("Groep 3: Buy a Ride")

def Main():
    # Create initial game instance
    menu = Menu()
    game = Game(4)

    # Event loop
    while True:
        # Calculate
        # Background white
        pygame.display.get_surface().fill((255, 255, 255))

        if app_state.state == "Menu":
            menu.index()

        elif app_state.state == "Rules":
            menu.rules()

        elif app_state.state == "Options":
            menu.options()
        
        elif app_state.state == "PlayerSelect":
            menu.playerSelect()

        elif app_state.state == "Game":
            game.run()

        elif app_state.state == "Pause":
            game.pause()

        event_handler.run()

Main()