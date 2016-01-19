import pygame
from time import sleep
from pygame.locals import *
from Game import *

pygame.init()
size = width, height = 600, 600
white = 255, 255, 255
green = 50, 255, 100
yellow = 255, 255, 0
screen = pygame.display.set_mode(size)
offset = 50
size = 10
background = pygame.Surface(screen.get_size())
background = background.convert()

# Screen title
pygame.display.set_caption("Buy a Ride")

def Main():
    game = Game()

    # Event loop
    while True:

        # Events
        for event in pygame.event.get():
            if event.type == QUIT:
                game.exit()

            if event.type == K_ESCAPE:
                game.pause()
                print("test")

            # DEBUG
            if event.type == MOUSEBUTTONDOWN:
                game.start()

        if game.state == "Menu":
            # Render menu
            background.fill(green)
            font = pygame.font.Font(None, 36)
            text = font.render("Menu", 1, (10, 10, 10))
            textpos = text.get_rect()
            textpos.centerx = background.get_rect().centerx
            background.blit(text, textpos)

        if game.state == "Game":
            # Show game
            background.fill(yellow)
            font = pygame.font.Font(None, 36)
            text = font.render("Game", 1, (10, 10, 10))
            textpos = text.get_rect()
            textpos.centerx = background.get_rect().centerx
            background.blit(text, textpos)

            if game.paused == True:
                pass

        # Render
        screen.blit(background, (0, 0))
        pygame.display.flip()

        sleep(0.2)

Main()