import time
from threading import Thread
import os, pygame
import time
from UIToolKit.MainMenu import *
from UIToolKit.ImageUtils import *

pygame.init()

def Main():
    start = time.time()
    mainMenu = MainMenu()
    #menu
    #ingame
    #paused game



    while True:
        for event in pygame.event.get(): # event handling loop
            mainMenu.handleInputs(event)

        mainMenu.draw()

        pygame.display.flip()
        time.sleep(0.2)
    
Main()