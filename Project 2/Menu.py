import pygame
from UIToolKit.Button import *
from UIToolKit.ImageUtils import *

class Menu(object):

    
    def __init__(self, background, appstate):        
        self.background = background
        self.ButtonList = []  
        #Can't we do this better?
        self.App = appstate
        self.load()

    def load(self):
        startButton = Button(ImageUtils.Screen.get_width() / 2 - 100, 50, 200, 100, "normal_example.png", "hover_example.png", "pressed_example.png", self.startGameFunc)
        self.ButtonList.append(startButton)
        settingsButton = Button(ImageUtils.Screen.get_width() / 2 - 100, startButton.PositionY + 200, 200, 100, "normal_example.png", "hover_example.png", "pressed_example.png", self.settingsFunc)
        self.ButtonList.append(settingsButton)
        quitButton = Button(ImageUtils.Screen.get_width() / 2 - 100, settingsButton.PositionY + 200, 200, 100, "normal_example.png", "hover_example.png", "pressed_example.png", self.quitFunc)
        self.ButtonList.append(quitButton)

    def startGameFunc(self):
        self.App.start()

    def settingsFunc(self):
        print("Open Settings menu here :D")

    def quitFunc(self):
        self.App.exit()
       

    def draw(self):
        for button in self.ButtonList:
            button.draw()

    def handleInputs(self, event):
        for button in self.ButtonList:
            button.handleInputEvents(event)


