import pygame
from Init import *

class Image:
    def __init__(self, filename, application_state = None, position = (0,0), size = None):
        global event_handler, app_state
        
        self.event_handler = event_handler
        self.global_state = app_state

        self.folder = "Content/"
        self.screen = pygame.display.get_surface()
        self.visible = True
        
        self.size = size
        self._position = position
        self.application_state = application_state

        self.filename = {'default': filename}
        self.image = {}

        self.click_parameter = None
        self.hover_parameter = None
        self.toggle_parameter = None
        self.toggled_state = False

        self.rect = None
        self.src()

    # Load image
    def src(self, filename = None, state = 'default'):
        # Fallback to default image
        if filename == None:
            filename = self.filename['default']
        else:
            self.filename[state] = filename

        # Load image and allow opacity
        image = pygame.image.load(self.folder + filename).convert_alpha()

        # Set size
        if self.size == None:
            self.size = image.get_rect().size

        image = pygame.transform.smoothscale(image, self.size)
        self.image[state] = image

        # only setup on initial load
        if state == 'default':
            self.position(self._position)
            self.rect = pygame.Rect(self._position[0], self._position[1], image.get_rect().width, image.get_rect().height)

        return self

    def hover(self, filename = None, function = None, parameter = None):
        self.filename['hover'] = filename

        # add to event listener
        event_handler.on('hover', [self._set_hover, function], self.rect, self.application_state, parameter)

        return self

    def _set_hover(self, parameter = None):
        self._set_image('hover')
        self.hover_parameter = parameter
        return self

    def click(self, filename = None, function = None, parameter = None):
        self.filename['click'] = filename

        # add to event listener
        event_handler.on('click', [self._set_click, function], self.rect, self.application_state, parameter)

        return self

    def _set_click(self, parameter = None):
        self._set_image('click')
        self.click_parameter = parameter
        return self

    def _set_image(self, state):
        self.src(self.filename[state], state).draw(state)

        return self

    def toggle(self, filename = None, function = None, parameter = None):
        self.filename['toggle'] = filename
        event_handler.on('toggle', [self._set_toggle, function], self.rect, self.application_state, parameter)

        return self
    
    def _set_toggle(self, parameter = None):
        if(self.toggled_state == True):
            self._set_image('default')
            self.toggle_parameter = parameter
            self.toggled_state = False
        else:
            self._set_image('toggle')
            self.toggle_parameter = parameter
            self.toggled_state = True

        app_state.next()
        return self

    def visible(self, visibility):
        self.visible = visibility

    def position(self, position):
        x = position[0]
        y = position[1]

        if x == 'center':
            x = (self.screen.get_width() - self.image['default'].get_rect().width) / 2
        
        if y == 'center':
            y = (self.screen.get_height() - self.image['default'].get_rect().height) / 2

        self._position = (x, y)
        return self

    # Show image
    def draw(self, state = 'default'):

        if self.toggled_state:
            state = 'toggle'

        if self.image[state] != None and self.visible == True:
            if self.application_state == self.global_state.state:
                self.screen.blit(self.image[state], self._position)

        return self
