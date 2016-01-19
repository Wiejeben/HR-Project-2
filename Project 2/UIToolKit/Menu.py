from UIToolKit.Button import *
from UIToolKit.ImageUtils import *

import pygame

class Menu():
   

    def __init__(self, amountOfButtons, background):
        self.AmountOfButtons = amountOfButtons
        self.Background = background
        self.ButtonList = []
    
    def quitfunc(self):
        quit()
    

    def MakeButtons(self):
        for x in range(0, 3):
            button = Button(ImageUtils.Screen.get_width() /2 - 100 ,200 * x + 50, 200,100, "normal_example.png", "hover_example.png", "pressed_example.png", self.quitfunc)
            self.ButtonList.append(button)
   

    def draw(self):
        for button in self.ButtonList:
            button.draw()

    def handleInputs(self, event):
        for button in self.ButtonList:
            button.handleInputEvents(event)

 

