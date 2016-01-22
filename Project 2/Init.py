﻿import pygame
from Library.EventHandler import *
from AppState import *

pygame.init()
pygame.display.set_mode((1024, 768))
pygame.time.Clock().tick(30) # Limit to 30 fps
event_handler = EventHandler('get')
app_state = AppState()