import pygame
from pygame.locals import *
from UIToolKit.Image import *

class EventHandler():
    def __init__(self, mode = 'wait'):
        self.mode = mode
        self.actions = []

    # When something happens
    def event(self):

        if self.mode == 'wait':
            event = pygame.event.wait()

        if event.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
            return False

        for action in self.actions:
            if action.region.collidepoint(event.pos) and action.type(event.type):
                for function in action.functions:
                    if function != None:
                        function()

    # Add new event
    def on(self, trigger, action, region = None):
        self.actions.append(Event(trigger, action, region))

class Event():
    def __init__(self, trigger, functions = [], region = None):
        self.trigger = trigger
        self.functions = functions
        self.region = region

    def type(self, type):
        trigger = self.trigger

        if trigger == 'hover':
            print('hover')
            return True

        elif trigger == 'click' and type == MOUSEBUTTONDOWN:
            return True