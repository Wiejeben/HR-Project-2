from Entities import *
from Library.Image import *
from Library.Text import *

class Player:
    def __init__(self, isRealPlayer, index = 0):
        self.isRealPlayer = isRealPlayer
        self.position = 0
        self.money = 10000

        self.player_class = 1

        # Pawn
        self.color = self._get_color(index)
        self.pawn = Image("pieces/" + self.color + "/piece.png", 'Game')

        # Personal board
        self.inventory_offset = index * 200
        self.board = Image("board/player_board.png", 'Game', (700,self.inventory_offset), (360,200))
        self.attractions = {}
        self.labels = {
            'username': Text("Player " + str(index + 1), 25, (0, 0, 0), (1080, self.inventory_offset + 80)),
            'money': Text(str(self.money) + "$", 25, (0, 0, 0), (1080, self.inventory_offset + 100))
        }

    def calculate_player_class(self):
        if self.money <= 10000:
            self.player_class = 1
        elif self.money >= 10000 and self.money <= 25000:
            self.player_class = 2
        elif self.money >= 25000 and self.money <= 40000:
            self.player_class = 3
        elif self.money >= 40000 and self.money <= 65000:
            self.player_class = 4
        elif self.money >= 65000:
            self.player_class = 5

    def _get_color(self, index):
        # List of colours
        player_color = ["green", "blue", "red", "yellow"]

        return player_color[index]

    def calculate_salary(self):
        for attraction in self.attractions:
            self.money += (attraction.price / 20)

    def buy_attraction(self, attraction, position):
        if self.money > attraction.price:
            self.money -= attraction.price
            self.attractions[attraction] = position

    def draw(self, position):
        # Draw pawn and personal board
        self.pawn.position((position.X, position.Y)).draw()
        self.board.draw()

        # Draw all attractions
        for index, attraction in enumerate(self.attractions):
            attraction.draw(index, self.inventory_offset + 15)

        # Update money label
        self.labels['money'].set_text(str(self.money) + "$")

        # Draw player name with money amount
        for index, value in self.labels.items():
            value.draw()

class Attraction:
    def __init__(self, name, price, type):
        self.name = name
        self.price = price
        self.type = type
        self.attraction = Image("attractions/" + str(self.type) + ".png", 'Game', (0,0), (60, 60))

    def draw(self, index, top):
        # Move to next row
        if index >= 6:
            top = top + 105

        self.attraction.position((700 + (index % 6 * 60), top)).draw()