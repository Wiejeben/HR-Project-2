from pygame import quit

class Game:
    def __init__(self):
        self.state = "Menu"
        self.paused = False

    # Close game
    def exit(self):
        pygame.quit()
    
    # Get inside game
    def start(self):
        self.state = "Game"

    # Interrupt gameplay
    def pause(self):
        if self.state == "Game":
            self.paused = True
    
    # Resume gameplay
    def resume(self):
        self.paused = False