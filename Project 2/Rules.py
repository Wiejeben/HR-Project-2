import pygame
from UIToolKit.Button import *
from UIToolKit.ImageUtils import *

class Rules(object):

    
    def __init__(self, background, appstate):        
        self.background = background
        self.ButtonList = []  
        #Can't we do this better?
        self.App = appstate
        self.load()

    def load(self):
        startButton = Button(ImageUtils.Screen.get_width() / 2 - 100, 50, 200, 100, "normal_example.png", "hover_example.png", "pressed_example.png", self.startGameFunc)
        self.ButtonList.append(startButton)
    def startGameFunc(self):
        self.App.start()
       

    def draw(self):
        ImageUtils.Screen.blit(self.background, (0,0))
        for button in self.ButtonList:
            button.draw()

    def handleInputs(self, event):
        for button in self.ButtonList:
            button.handleInputEvents(event)


