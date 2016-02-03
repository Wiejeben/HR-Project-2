from Entities import *
from Library.Image import *
from Library.Text import *

class Player:
    def __init__(self, isRealPlayer, index = 0):
        self.isRealPlayer = isRealPlayer
        self.isActive = False
        self.position = 0
        self.money = 10000
        self.index = index

        self.player_class = 1
        self.defect_turn = 0

        # Pawn
        self.color = self._get_color(index)
        self.pawn = Image("pieces/" + self.color + "/piece.png", 'Game')

        # Personal board
        self.inventory_offset = index * 194
        self.board = Image("board/player_board.png", 'Game', (700,self.inventory_offset), (360,194))
        self.board_active = Image("board/player_board_active.png", 'Game', (700,self.inventory_offset), (360,194))
        self.attractions = {}
        self.labels = {
            'username': Text("Player " + str(index + 1), 25, (0, 0, 0), (1080, self.inventory_offset + 40)),
            'money': Text(str(self.money) + "$", 25, (0, 0, 0), (1083, self.inventory_offset + 60))
        }

        self.pawn_icon = Image("pieces/" + self.color + "/piece.png", 'Game', (1100, self.inventory_offset + 110))

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
            self.money += int(attraction.price / 20)

    def attraction_buy(self, attraction, position):
        self.money -= attraction.price
        attraction.owner = self
        self.attractions[attraction] = position

    def draw(self, position):
        # Draw and reposition pawn
        if self.position < 10:
            self.pawn.position((position.X, position.Y + self.index * 15)).draw()
        elif self.position < 20:
            self.pawn.position((position.X + self.index * 15, position.Y)).draw()
        elif self.position < 30:
            self.pawn.position((position.X, position.Y + self.index * 15)).draw()
        elif self.position < 40:
            self.pawn.position((position.X - 45 + self.index * 15, position.Y + self.index)).draw()

        # Draw personal board
        if self.isActive:
            self.board_active.draw()
            self.pawn_icon.draw()
        else:
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
        self.owner = None
        self.type = type
        self.attraction = Image("attractions/" + str(self.type) + ".png", 'Game', (0,0), (60, 60))

    def draw(self, index, top):
        # Move to next row
        if index >= 6:
            top = top + 105

        self.attraction.position((700 + (index % 6 * 60), top)).draw()