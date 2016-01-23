import pygame

class AppState:
    def __init__(self):
        self.state = "Menu"
        self.paused = False
        self.temp_state = None

    def set_state(self, state):
        self.temp_state = state

    def switch_state(self):
        if self.temp_state != None:
            self.state = self.temp_state
            print("Set: " + self.temp_state)
            self.temp_state = None

    def menu(self):
        self.set_state("Menu")
        print("menu")
        self.next()

    def rules(self):
        self.set_state("Rules")
        print("rules set")
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

    # Interrupt gameplay
    def togglePause(self):
        print("Toggle pause")
        if self.state == "Game":

            if self.paused:
                self.paused = False
            else:
                self.paused = True
    
    # Resume gameplay
    def resume(self):
        self.paused = False