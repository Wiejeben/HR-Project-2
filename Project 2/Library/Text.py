import pygame

class Text():
    def __init__(self, content, size = 25, color = (0, 0, 0), position = (0, 0), background = None):
        self.screen = pygame.display.get_surface()

        # List internal properties
        self.content = content
        self.size = size
        self.color = color
        self._position = position
        self.background = background

        self._text = pygame.font.Font(None, size).render(content, 1, color, background)
        self._rect = None
        self.position()

    def position(self, position = None):
        if position == None:
            position = self._position

        x = position[0]
        y = position[1]

        if x == 'center':
            x = (self.screen.get_width() - self._text.get_rect().width) / 2
        
        if y == 'center':
            y = (self.screen.get_height() - self._text.get_rect().height) / 2

        self._position = (x, y)
        return self

    def set_text(self, text):
        self._text = pygame.font.Font(None, self.size).render(str(text), 1, self.color, self.background)

    def draw(self):
        return self.screen.blit(self._text, self._position)

