﻿import pygame
from Library.EventHandler import *
from Library.AppState import *

pygame.init()
pygame.mixer.init()
pygame.display.set_mode((1170, 768))
pygame.time.Clock().tick(15) # Limit fps
app_state = AppState()
event_handler = EventHandler(app_state)
