# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from random import randint

class Board:

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []
    
    def print(self):
        for row in self.board:
            print(" ".join(row))

    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"
    
    def add_ship(self, x, y, type = "Computer"):
        if len(self.ships) >= self.num_ships:
            print("Error")
        else:
            self.ships.append((x,y))
            if self.type == "Player":
                self.board[x][y] = "@"



def load_game():
    """
    Loads up main start menu for the user.
    Giving them the option to start a game or not.
    Also outlines the game rules.
    """
    print("Welcome to Battleships!\n")
    print("A turn based game, where user and computer take turns to guess")
    print("where each others Battleships are.")
    print("The winner is whoever sinks all their oppenents Battleships first!\n")
    print("Are you ready to Battle!? Y/N\n")
    
def start_game():
    x = input()
    if x == "Y":
        map_size()
    elif x == "N":
        exit()
    else:
        print("Please enter Y/N\n")


def map_size():
    print("Please choose your map size, 6, 8 or 10!\n")
    size = input()
    if size == "6":
        print("Game size 6")
        return size
    elif size == "8":
        print("Game size 8")
        return size
    elif size == "10":
        print("Game size 10")
        return size
    else:
        print("Please choose your grid size!\n")
        map_size()


def main():

    load_game()
    start_game()

    size = map_size()
    num_ships = 4
    scores["Computer"] = 0
    scores["Player"] = 0

    computer_board = Board(size, num_ships, "Computer", type="Computer")
    player_board = Board(size, num_ships, "Player", type = "Player")

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)

    play_game(computer_board, player_board)


main()