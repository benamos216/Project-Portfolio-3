# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from random import randint
from random import random

#Player Board for holding ship locations
HIDDEN_BOARD = [[" "] * 8 for x in range(8)]
#Player Board for displaying hits and misses
GUESS_BOARD = [[" "] * 8 for i in range(8)]
#Computer Board for holding ship locations
COMPUTER_BOARD = [[" "] * 8 for x in range(8)]
#Computer Board for displaying hits and misses
COMPUTER_PLAY_BOARD = [[" "] * 8 for i in range(8)]

def print_board(board):
    """
    Generates an 8 x 8 grid to display the game as it goes along
    A - H letters used for the columns, 1 - 8 used for the rows
    """
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}

def create_ships(board):
    """
    Randomly generates 5 ships on both players boards
    """
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"

def get_ship_location():
    """
    Player input for their guesses. Checks that each input is valid
    and informs the player if they are made an incorrect input.
    """
    row = input("Enter the row of the ship: ").upper()
    while row not in "12345678":
        print('Not an appropriate choice, please select a valid row')
        row = input("Enter the row of the ship: ").upper()
    column = input("Enter the column of the ship: ").upper()
    while column not in "ABCDEFGH":
        print('Not an appropriate choice, please select a valid column')
        column = input("Enter the column of the ship: ").upper()
    return int(row) - 1, letters_to_numbers[column]

def computer_turn():
    """
    Generates the computer's turn, by randomly picking a row
    and column value within the parameters of the grid.
    """
    row = randint(1,8)
    column = randint(1,8)
    return int(row) - 1, int(column) - 1


def count_hit_ships(board):
    """
    Checks if all the ships on the board have been hit
    """
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

def play_game():
    create_ships(HIDDEN_BOARD)
    create_ships(COMPUTER_BOARD)
    while count_hit_ships(GUESS_BOARD) < 6:
        print('Guess a battleship location\n')
        print('Player Board\n')
        print_board(GUESS_BOARD)
        row, column = get_ship_location()
        if GUESS_BOARD[row][column] == "-":
            print("You guessed that one already.")
        elif HIDDEN_BOARD[row][column] == "X":
            print("Hit\n")
            GUESS_BOARD[row][column] = "X"
            print("Player Board\n")
            print_board(GUESS_BOARD)
        else:
            print("MISS!\n")
            GUESS_BOARD[row][column] = "-"
            print("Player Board\n")
            print_board(GUESS_BOARD)
        if count_hit_ships(GUESS_BOARD) == 5:
            print("You win!")
            GUESS_BOARD[row][column] = "X"
            exit()
        while count_hit_ships(COMPUTER_PLAY_BOARD) < 6:
            print('\nComputer Board\n')
            print_board(COMPUTER_PLAY_BOARD)
            row, column = computer_turn()
            if COMPUTER_PLAY_BOARD[row][column] == "-":
                print("You guessed that one already.")
            elif COMPUTER_BOARD[row][column] == "X":
                print("Hit\n")
                COMPUTER_PLAY_BOARD[row][column] = "X"
                print("Computer Board\n")
                print_board(COMPUTER_PLAY_BOARD)
            else:
                print("MISS!\n")
                COMPUTER_PLAY_BOARD[row][column] = "-"
                print("Computer Board\n")
                print_board(COMPUTER_PLAY_BOARD)
            if count_hit_ships(COMPUTER_PLAY_BOARD) == 5:
                print("You Lose!")
                COMPUTER_PLAY_BOARD[row][column] = "X"
                exit()
            break
            

play_game()