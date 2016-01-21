import pygame
from UIToolKit.ImageUtils import *
from pygame.locals import *


class Button:
    def __init__(self, x, y, width, height, normalState=None, mouseoverState=None, mouseclickState=None, function=None):
        self.PositionX = x
        self.PositionY = y
        self.Width = width
        self.Height = height

        self.MouseDown = False
        self.MouseOver = False
        self.MouseClicked = False
        self.PrevMouseOverButton = False
        self.FunctionToExecute = function
        self.Rectangle = pygame.Rect(x, y, width, height)

        #Load button images
        normalB = ImageUtils.loadImage("buttons/" + normalState)
        self.NormalImage = ImageUtils.scale(normalB, self.Rectangle)

        mouseoverB = None
        if mouseoverState != None:
            mouseoverB = ImageUtils.loadImage("buttons/" + mouseoverState)
            self.MouseOverImage = ImageUtils.scale(mouseoverB, self.Rectangle)

        clickedB = None
        if mouseclickState != None:
            clickedB = ImageUtils.loadImage("buttons/" + mouseclickState)
            self.ClickedImage = ImageUtils.scale(clickedB, self.Rectangle)
        

    def handleInputEvents(self, event):
        if event.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
            return []

        if not self.MouseOver and self.Rectangle.collidepoint(event.pos):
            self.MouseOver = True

        elif self.MouseOver and not self.Rectangle.collidepoint(event.pos):
            self.MouseOver = False

        if self.Rectangle.collidepoint(event.pos):
             if event.type == MOUSEBUTTONDOWN:
                self.MouseDown = True
                self.PrevMouseOverButton = True

             else:
                if event.type in (MOUSEBUTTONUP, MOUSEBUTTONDOWN):
                    self.PrevMouseOverButton = False

             doMouseClick = False
             if event.type == MOUSEBUTTONUP:
                if self.PrevMouseOverButton:
                    doMouseClick = True

                self.PrevMouseOverButton = False

                if self.FunctionToExecute != None:
                    self.FunctionToExecute()

                if self.MouseDown:
                    self.MouseDown = False

                if doMouseClick:
                    self.MouseDown = False

    def draw(self):
        orange = 255, 100, 0
        ImageUtils.Screen.fill(orange)

        if self.MouseDown:
            ImageUtils.Screen.blit(self.ClickedImage, self.Rectangle)

        elif self.MouseOver:
            ImageUtils.Screen.blit(self.MouseOverImage, self.Rectangle)

        else:
            ImageUtils.Screen.blit(self.NormalImage, self.Rectangle)

    def __iter__(self):
        return self
