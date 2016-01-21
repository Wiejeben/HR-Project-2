import pygame

class AppState:
    def __init__(self):
        self.state = "Menu"
        self.paused = False

    # Close game
    def exit(self):
        pygame.quit()
    
    # Get inside game
    def start(self):
        self.state = "Game"

    # Go inside settings page
    def settings(self):
        self.state = "Settings"

    # Interrupt gameplay
    def toggle_pause(self):
        if self.state == "Game":

            if self.paused:
                self.paused = False
            else:
                self.paused = True
    
    # Resume gameplay
    def resume(self):
        self.paused = False