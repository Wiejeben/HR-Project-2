import pygame
from pygame.locals import *
from Library.Image import *
from time import sleep

class EventHandler():
    def __init__(self, mode = 'wait', speed = 0):
        self.mode = mode
        self.actions = []
        self.speed = speed

    # When something happens
    def begin(self):

        if self.mode == 'wait':
            event = pygame.event.wait()

        # Prevent events that got no POS on it
        if event.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
            return False

        for action in self.actions:
            if action.region.collidepoint(event.pos) and action.type(event.type):
                for function in action.functions:
                    if function != None:
                        function()

    def end(self):
        pygame.display.flip()
        sleep(self.speed)

    # Add new event
    def on(self, trigger, action, region):
        self.actions.append(Event(trigger, action, region))

class Event():
    def __init__(self, trigger, functions = [], region = None):
        self.trigger = trigger
        self.functions = functions
        self.region = region

    def type(self, type):
        trigger = self.trigger

        if trigger == 'hover':
            return True

        elif trigger == 'click' and type == MOUSEBUTTONDOWN:
            return True