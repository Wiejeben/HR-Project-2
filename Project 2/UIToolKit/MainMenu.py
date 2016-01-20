from UIToolKit.Button import *
from UIToolKit.ImageUtils import *

import pygame

class MainMenu():

    def __init__(self):
        self.ButtonList = []  
        self.MakeButtons()

    def startGameFunc(self):
        print("Starting Game, implement something interesting here")

    def settingsFunc(self):
        print("Open Settings menu here :D")

    def quitFunc(self):
        quit()

    def MakeButtons(self):
        startButton = Button(ImageUtils.Screen.get_width() / 2 - 100, 50, 200, 100, "normal_example.png", "hover_example.png", "pressed_example.png", self.startGameFunc)
        self.ButtonList.append(startButton)
        settingsButton = Button(ImageUtils.Screen.get_width() / 2 - 100, startButton.PositionY + 200, 200, 100, "normal_example.png", "hover_example.png", "pressed_example.png", self.settingsFunc)
        self.ButtonList.append(settingsButton)
        quitButton = Button(ImageUtils.Screen.get_width() / 2 - 100, settingsButton.PositionY + 200, 200, 100, "normal_example.png", "hover_example.png", "pressed_example.png", self.quitFunc)
        self.ButtonList.append(quitButton)

    def draw(self):
        for button in self.ButtonList:
            button.draw()

    def handleInputs(self, event):
        for button in self.ButtonList:
            button.handleInputEvents(event)

 

