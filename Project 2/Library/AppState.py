import pygame

class AppState:
    def __init__(self):
        self.state = "Menu"
        self.temp_state = None

    def set_state(self, state):
        self.temp_state = state

    def switch_state(self):
        if self.temp_state != None:
            self.state = self.temp_state
            self.temp_state = None

    def menu(self):
        self.set_state("Menu")
        self.next()

    def rules(self):
        self.set_state("Rules")
        self.next()

    def options(self):
        self.set_state("Options")
        self.next()

    # Go to next frame
    def next(self):
        pygame.event.post(pygame.event.Event(pygame.locals.USEREVENT))

    # Close game
    def exit(self):
        exit()
    
    # Get inside game
    def start(self):
        self.set_state("Game")
        self.next()

    def pause(self):
        if self.state == "Game":
            self.set_state("Pause")

        if self.state == "Pause":
            self.set_state("Game")

        self.next()
    
    # Resume gameplay
    def resume(self):
        self.paused = False