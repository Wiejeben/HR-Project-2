﻿import pygame
from Library.Image import *
from Init import *
from Library.EventHandler import *
from Library.AppState import *
from Game import *
from Menu import *

# Screen title
pygame.display.set_caption("Monocoasterweg by Groep 3")

def Main():
    # Create initial game instance
    menu = Menu()
    game = None

    while True:
        # Clear surface
        pygame.display.get_surface().fill((255, 255, 255))

        # Pause when we are not ingame
        if app_state.state != "Game":
            pygame.mixer.music.pause()

        if app_state.state == "Game":
            game.update()
            game.draw()
            pygame.mixer.music.unpause()

        elif app_state.state == "Menu":
            menu.index()

        elif app_state.state == "Rules":
            menu.rules()

        elif app_state.state == "Options":
            menu.options()

        elif app_state.state == "PlayerSelect":
            menu.playerSelect()

        elif app_state.state == "GameStart":
            game = Game(app_state.player_amount)
            app_state.state = "Game"

        elif app_state.state == "Pause":
            game.screen_pause()

        elif app_state.state == "Won":
            game.screen_winner()

        event_handler.run()

Main()