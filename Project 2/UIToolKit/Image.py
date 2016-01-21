import pygame
from Init import *

class Image:
    def __init__(self, path, pos = (0, 0), size = None):
        self.folder = "Content/"
        self.screen = pygame.display.get_surface()

        global event_handler
        self.event_handler = event_handler

        
        self.size = size
        self._pos = pos
        self.image = None

        # Set default image and render it
        self.path = path
        self.src()

    # Load image
    def src(self, path = None):
        #print(path)
        # Set element
        if path == None:
            path = self.path

        # Load image
        entry = pygame.image.load(self.folder + path).convert_alpha()

        # Set size and position
        if self.size == None:
            self.size = entry.get_rect().size

        self.image = pygame.transform.smoothscale(entry, self.size)
        self.position = self._position(self._pos)
        self.rect = pygame.Rect(self.position[0], self.position[1], self.image.get_rect().width, self.image.get_rect().height)

        return self

    def hover(self, path, action = None):
        # add to event listener
        event_handler.on('hover', [self.src(path).draw, action], self.rect)

        return self

    def click(self, function):
        # add to event listener
        event_handler.on('click', [function], self.rect)

        return self

    def _position(self, pos):
        x = pos[0]
        y = pos[1]

        if x == 'center':
            x = (self.screen.get_width() - self.image.get_rect().width) / 2
        
        if y == 'center':
            y = (self.screen.get_height() - self.image.get_rect().height) / 2

        return (x, y)

    # Show image
    def draw(self):
        if self.image != None:
            self.screen.blit(self.image, self.position)

        return self
