# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

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
        create_game()
    elif x == "N":
        exit()
    else:
        print("Please enter Y/N\n")
        start_game()


def create_game():
    print("Game starting up....\n")


def main():
    load_game()
    start_game()

main()