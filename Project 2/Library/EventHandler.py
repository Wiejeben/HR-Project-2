import pygame
from pygame.locals import *
from Library.Image import *
from time import sleep

class EventHandler():
    def __init__(self, app_state, mode = 'wait', speed = 0):
        self.mode = mode
        self.actions = []
        self.speed = speed

        self.app_state = app_state

    # When something happens
    def begin(self):
            
        if self.mode == 'get':
            events = pygame.event.get()

            if len(events) == 0:
                self._check_events()

            for event in events:
                self._check_events(event)
        else:
            self._check_events(pygame.event.wait())
        
    def _check_events(self, event = None):
        event_type = None
        if event != None:
            event_type = event.type

        for action in self.actions:
            if action.region.collidepoint(pygame.mouse.get_pos()) and action.type(event_type):
                for function in action.functions:
                    if function != None:
                        function()

    def end(self):
        pygame.display.flip()
        self.app_state.switch_state()
        sleep(self.speed)

    # Add new event
    def on(self, trigger, action, region, state):
        self.actions.append(Event(trigger, action, region, state, self.app_state))

class Event():
    def __init__(self, trigger, functions = [], region = None, element_state = None, app_state = None):
        self.trigger = trigger
        self.functions = functions
        self.region = region
        self.element_state = element_state
        self.app_state = app_state

    def type(self, type):
        if self.element_state != self.app_state.state:
            return False

        trigger = self.trigger

        if trigger == 'hover':
            return True
        elif trigger == 'click' and type == MOUSEBUTTONUP:
            return True

        return False
