import pygame
from time import sleep
from pygame.locals import *
from AppState import *

size = width, height = 600, 600
white = 255, 255, 255
green = 50, 255, 100
yellow = 255, 255, 0
orange = 255, 100, 0
offset = 50
size = 10

pygame.init()
screen = pygame.display.set_mode(size)

background = pygame.Surface(screen.get_size())
background = background.convert()

# Screen title
pygame.display.set_caption("Groep 3: Buy a Ride")

def Main():
    # Create initial game instance
    app = AppState()
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
            background.fill(green)
            font = pygame.font.Font(None, 36)
            text = font.render("Menu", 1, (10, 10, 10))
            textpos = text.get_rect()
            textpos.centerx = background.get_rect().centerx
            background.blit(text, textpos)

        elif app.state == "Game":
            # Show game
            background.fill(yellow)
            font = pygame.font.Font(None, 36)
            text = font.render("Game", 1, (10, 10, 10))
            textpos = text.get_rect()
            textpos.centerx = background.get_rect().centerx
            background.blit(text, textpos)

            while app.paused:
                print("Paused")
                
                background.fill(orange)
                font = pygame.font.Font(None, 36)
                text = font.render("Paused!", 1, (10, 10, 10))
                textpos = text.get_rect()
                textpos.centerx = background.get_rect().centerx
                background.blit(text, textpos)

                sleep(speed)

        # Render
        screen.blit(background, (0, 0))
        pygame.display.flip()

        # Run at 5 FPS
        sleep(speed)

Main()