import pygame
from Init import *

class Image:
    def __init__(self, path, pos = (0, 0), size = None):
        self.folder = "Content/"
        self.screen = pygame.display.get_surface()

        global event_handler
        self.event_handler = event_handler

        global app_state
        self.app_state = app_state
        
        self.size = size
        self._pos = pos
        self.image = None
        self.image_hover = None
        self.hover_state = None

        # Set default image and render it
        self.path = path
        self.src()

    # Load image
    def src(self, path = None, state = None):
        #print(path)
        # Set element
        if path == None:
            path = self.path

        # Load image
        image = pygame.image.load(self.folder + path).convert_alpha()

        # Set size and position
        if self.size == None:
            self.size = image.get_rect().size

        image = pygame.transform.smoothscale(image, self.size)

        if state == 'hover':
            self.image_hover = image
        else:
            self.image = image

        self.position = self._position(self._pos)
        self.rect = pygame.Rect(self.position[0], self.position[1], image.get_rect().width, image.get_rect().height)

        return self

    def hover(self, path, state = None, action = None):
        # add to event listener
        self.path_hover = path
        self.hover_state = state

        event_handler.on('hover', [self._set_hover, action], self.rect)

        return self

    def _set_hover(self):
        self.src(self.path_hover, 'hover').draw('hover')

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
    def draw(self, state = None):
        if self.path == "buttons/Start.png":
            if state == 'hover':
                print('hover')
            else:
                print('else')

        if state == 'hover':
            image = self.image_hover
        else:
            image = self.image

        if image != None:
            if self.hover_state == self.app_state.state:
                self.screen.blit(image, self.position)

        return self
