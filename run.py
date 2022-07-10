# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from random import randint

#Board for holding ship locations
HIDDEN_BOARD = [[" "] * 8 for x in range(8)]
# Board for displaying hits and misses
GUESS_BOARD = [[" "] * 8 for i in range(8)]

COMPUTER_BOARD = [[" "] * 8 for x in range(8)]

COMPUTER_PLAY_BOARD = [[" "] * 8 for i in range(8)]

def print_board(board):
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
#computer create 5 ships
def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"

def get_ship_location():
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


#check if all ships are hit
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

def play_game():
    create_ships(HIDDEN_BOARD)
    create_ships(COMPUTER_BOARD)
    print('Guess a battleship location\n')
    print('Player Board\n')
    print_board(GUESS_BOARD)
    print('\nComputer Board\n')
    print_board(COMPUTER_PLAY_BOARD)
    while count_hit_ships(GUESS_BOARD) < 6, count_hit_ships(COMPUTER_PLAY_BOARD) < 6:
        print_board(GUESS_BOARD)
        print_board(COMPUTER_PLAY_BOARD)
        row, column = get_ship_location()
        row, column = computer_turn()
        if GUESS_BOARD[row][column] == "-":
            print("You guessed that one already.")
        elif HIDDEN_BOARD[row][column] == "X":
            print("Hit")
            GUESS_BOARD[row][column] = "X" 
        else:
            print("MISS!")
            GUESS_BOARD[row][column] = "-"      
        if count_hit_ships(GUESS_BOARD) == 5:
            print("You win!")
            GUESS_BOARD[row][column] = "X"
            break
            

play_game()