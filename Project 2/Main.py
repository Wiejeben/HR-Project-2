﻿import pygame
from time import sleep
from pygame.locals import *
from AppState import *
from Game import *
from Menu import *

canvasSize = width, height = 600, 600

white = 255, 255, 255
green = 50, 255, 100
yellow = 255, 255, 0
orange = 255, 100, 0

offset = 50
size = 10

pygame.init()
screen = pygame.display.set_mode(canvasSize)

background = pygame.Surface(screen.get_size())
background = background.convert()

# Screen title
pygame.display.set_caption("Groep 3: Buy a Ride")

def Main():
    # Create initial game instance
    app = AppState()
    menu = Menu(background)
    game = Game(background)
    speed = 0.2

    # Event loop
    while True:

        # Events
        for event in pygame.event.get():
            if event.type == QUIT:
                app.exit()

            if event.type == MOUSEBUTTONDOWN:
                app.start()

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    app.togglePause()


        if app.state == "Menu":
            # Render menu
            menu.load()

        elif app.state == "Game":
            # Show game
            if app.paused:
                game.pause()
            else:
                game.load()

        # Render
        screen.blit(background, (0, 0))
        pygame.display.flip()

        # Run at 5 FPS
        sleep(speed)

Main()