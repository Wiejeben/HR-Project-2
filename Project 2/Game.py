import time
from threading import Thread
import os, pygame
import time
from UIToolKit.Menu import *
from UIToolKit.ImageUtils import *

pygame.init()

def Main():
    start = time.time()
    menu = Menu(3, "")
    menu.MakeButtons()
    #menu
    #ingame
    #paused game



    while True:
        for event in pygame.event.get(): # event handling loop
            menu.handleInputs(event)

        menu.draw()

        pygame.display.flip()
        time.sleep(0.2)
    
Main()