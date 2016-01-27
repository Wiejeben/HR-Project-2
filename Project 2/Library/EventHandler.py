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
    def run(self):
        # Perform actions
        if self.mode == 'get':
            events = pygame.event.get()

            if len(events) == 0:
                self._check_events()

            for event in events:
                self._check_events(event)
        else:
            self._check_events(pygame.event.wait())

        # End frame
        pygame.display.flip()
        self.app_state.switch_state()
        sleep(self.speed)
        
    def _check_events(self, event = None):
        if Event('esc').type(event):
            print('Pause')
            self.app_state.pause()

        elif Event('close').type(event):
            self.app_state.exit()

        for action in self.actions:
            if action.region.collidepoint(pygame.mouse.get_pos()) and action.type(event):
                for function in action.functions:
                    if function != None and action.parameter != None:
                        function(action.parameter)
                    elif function != None:
                        function()

    # Add new event
    def on(self, trigger, action, region, state, parameter):
        self.actions.append(Event(trigger, action, region, state, self.app_state, parameter))

class Event():
    def __init__(self, trigger, functions = [], region = None, element_state = None, app_state = None, parameter = None):
        self.trigger = trigger
        self.functions = functions
        self.region = region
        self.element_state = element_state
        self.app_state = app_state
        self.parameter = parameter

    def type(self, event):
        if self.element_state != None:
            if self.element_state != self.app_state.state:
                return False

        trigger = self.trigger

        if trigger == 'hover':
            return True

        if event != None:
            if trigger == 'click' and event.type == MOUSEBUTTONUP:
                return True
            elif trigger == 'close' and event.type == QUIT:
                return True
            elif event.type == KEYDOWN:
                if trigger == 'esc' and event.key == K_ESCAPE:
                    return True
            

        return False
