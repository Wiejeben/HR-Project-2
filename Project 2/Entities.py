import random
import pygame
from time import sleep
from Library.Image import *
from Library.Text import *

class Vector2D():
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __str__(self):
        return "(" + str(self.X) + ", " + str(self.Y) + ")"

class Dice():
    def __init__(self, position, size):
        self.number = 1
        self.position = position
        self.size = size
        self.texture = {
            1 : Image("dice/dice_1.png", 'Game', (self.position.X, self.position.Y)),
            2 : Image("dice/dice_2.png", 'Game', (self.position.X, self.position.Y)),
            3 : Image("dice/dice_3.png", 'Game', (self.position.X, self.position.Y)),
            4 : Image("dice/dice_4.png", 'Game', (self.position.X, self.position.Y)),
            5 : Image("dice/dice_5.png", 'Game', (self.position.X, self.position.Y)),
            6 : Image("dice/dice_6.png", 'Game', (self.position.X, self.position.Y))
        }

    def roll(self): 
        self.number = random.randint(1,6)

    def draw(self):
        self.texture[self.number].draw()

class GameTile:
    def __init__(self, position, interaction, type = None):
        self.position = position
        self.interaction = interaction
        self.type = type
        self.entity = self._set_entity()

    def _set_entity(self):
        i = self.interaction

        if i == "ThrillRides":
            return Attraction('3D Cinema', 10000, 'thrill_rides')

        elif i == "WaterRides":
            return Attraction('Boat Hire', 3000, 'water_rides')

        elif i == "TransportRides":
            return Attraction('Train', 5000, 'transport_rides')

        elif i == "GentleRides":
            return Attraction('Maze', 7500, 'gentle_rides')

        elif i == "Rollercoasters":
            return Attraction('Mine Train Coaster', 12500, 'rollercoaster')

        elif i == "ShopsAndStalls":
            return Attraction('Balloon Stall', 1900, 'shops_and_stalls')

        return None


class Attraction:
    def __init__(self, name, price, type):
        self.name = name
        self.price = price
        self.owner = None
        self.type = type
        self.attraction = Image("attractions/" + str(self.type) + ".png", 'Game', (0,0), (60, 60))

        self.labels = [
            Text("Ticket price " + str(int(self.price / 20)), 25, (0,0,0), (280, 725)),
            Text(str(self.price) + "$", 25, (255,255,255), (75, 725))
        ]

    def draw(self, index, top):
        # Move to next row
        if index >= 6:
            top = top + 105

        self.attraction.position((700 + (index % 6 * 60), top)).draw()

    def draw_specs(self, player_class):
        self.ticket_price.draw()

class ChanceCard:
    def __init__(self, texture, money):
        self.texture = Image(texture, 'Game', (180,350))
        self.money = money
    def draw(self):
        self.texture.draw()