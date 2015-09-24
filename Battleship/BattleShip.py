import os
import re
import random
import time

__author__ = 'Emma & Lee'


# '''
# Program Prologue
# '''


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: main()
#
#   Pre:
#
#   Post:
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    welcome_prompt()
    run_game()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: welcome_prompt()
#
#   Pre: None.
#
#   Post: Prints out lovely UI for the user.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def welcome_prompt():
    print 'WELCOME TO\n'
    print ' ____    __   ____  ____  __    ____  ___  _   _  ____  ____'
    print '(  _ \  /__\ (_  _)(_  _)(  )  ( ___)/ __)( )_( )(_  _)(  _ \\'
    print ' ) _ < /(__)\  )(    )(   )(__  )__) \__ \ ) _ (  _)(_  )___/'
    print '(____/(__)(__)(__)  (__) (____)(____)(___/(_) (_)(____)(__)'
    print '\nShips Available:'
    print '1 - Aircraft Carrier     (5 spaces)'
    print '1 - Battleship           (4 spaces)'
    print '1 - Submarine            (3 spaces)'
    print '1 - Patrol Boat          (2 spaces)\n\n'


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: run_game()
#
#   Pre:
#
#   Post:
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def run_game():
    # Initialize the board
    user_board = initialize_board(True)
    computer_board = initialize_board(False)

    # TODO REMOVE THESE
    print_out_board(user_board, True)
    print_out_board(computer_board, False)
    # TODO REMOVE THESE

    # While the game is NOT over, continue playing the game.
    while not is_game_over():
        print_out_board(user_board, True)
        make_move_user()
        is_ship_sunken()
        if is_game_over():
            print 'GAME OVER! You won! WOOHOO!'

        print_out_board(computer_board, False)
        make_move_comp()
        is_ship_sunken()
        if is_game_over():
            print 'GAME OVER! Computer beat ya...'


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: initialize_board()
#
#   Pre:
#
#   Post:
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def initialize_board(bool_user):
    # Checks if the input is lowercase y
    if bool_user:
        if raw_input('Would you like to have your ships auto-deployed? y or n: ').lower() == "y":
            # Obviously yes, so auto-place ships.
            return auto_place_ships()
        else:
            # Manually place them...false
            return manually_place_ships()
    else:
        return auto_place_ships()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: manually_place_ships()
#
#   Pre:
#
#   Post:
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def manually_place_ships():
    board = ([[' ' for z in range(10)] for z in range(10)])  # Initialize board's slots to ' '. A 10x10 board is made.
    ships = {"Aircraft carrier": 5, "Battleship": 4, "Submarine": 3, "Destroyer": 3, "Patrol boat": 2}  # Ship list

    for ship in ships.keys():
        valid = False
        count = 0
        placement = ""
        while not valid:  # Loop through the validation, choosing random numbers till spot is found.
            if count == 0:
                placement = raw_input('Please enter you coordinate points for ' + ship + ' (col, row, v/h): ').lower()
                count += 1  # Add 1 to the count
            else:
                placement = raw_input('Invalid placement, please try again for ' + ship + ' (col, row, v/h): ').lower()

            position = placement.strip('()')  # Remove the '(' and ')' if the user entered them.
            position = position.replace(' ', '')  # Remove all blank space.
            position = position.split(",")  # Position is now an array of strings.

            if position[2] != 'v' or position[2] != 'h':
                valid = False
                continue

            x = random.randint(0, 9)  # Choose random number 0-9
            y = random.randint(0, 9)
            o = random.randint(0, 1)
            valid = can_place(board, ships[ship], x, y, o)  # Make sure we can place the ship there.
        board = place_ship(board, ships[ship], ship[0], x, y, o)  # We passed the tests, place the ship at that spot

    return board


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: auto_place_ships()
#
#   Pre:
#
#   Post:
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def auto_place_ships():
    board = ([[' ' for z in range(10)] for z in range(10)])  # Initialize board's slots to ' '. A 10x10 board is made.
    ships = {"A": 5, "B": 4, "S": 3, "D": 3, "P": 2}  # Ship list

    for ship in ships.keys():
        valid = False
        while not valid:  # Loop through the validation, choosing random numbers till spot is found.
            x = random.randint(0, 9)  # Choose random number 0-9
            y = random.randint(0, 9)
            o = random.randint(0, 1)
            valid = can_place(board, ships[ship], x, y, o)  # Make sure we can place the ship there.
        board = place_ship(board, ships[ship], ship[0], x, y, o)  # We passed the tests, place the ship at that spot

    return board


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: can_place(list)
#
#   Pre:
#
#   Post:
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def can_place(board, ship, x, y, o):
    if o == 0 and x + ship > 10:  # Vertical
        return False
    elif o == 1 and y + ship > 10:  # Horizontal
        return False
    else:
        if o == 0:  # Vertical
            for i in range(ship):
                if board[x + i][y] != ' ':
                    return False
        elif o == 1:  # Horizontal
            for i in range(ship):
                if board[x][y + i] != ' ':
                    return False

    return True


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: place_ship(list)
#
#   Pre:
#
#   Post:
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def place_ship(board, ship, name, x, y, o):
    if o == 0:  # Vertical
        for i in range(ship):
            board[x + i][y] = name
    elif o == 1:  # Horizontal
        for i in range(ship):
            board[x][y + i] = name
    return board


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: make_move_user()
#
#   Pre:
#
#   Post:
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def make_move_user():
    print 'Make move user'


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: make_move_comp()
#
#   Pre:
#
#   Post:
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def make_move_comp():
    print 'Make move comp'


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: is_ship_sunken()
#
#   Pre:
#
#   Post:
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def is_ship_sunken():
    print 'is sunken'


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: is_game_over()
#
#   Pre:
#
#   Post:
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def is_game_over():
    print 'game over'
    return True


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: is_game_over()
#
#   Pre:
#
#   Post:
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def represents_int(string):
    return re.match(r"[-+]?\d+$", string) is not None


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: cls(#)
#   Pre:
#
#   Post:
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: number_to_letter(integer)
#
#   Pre:
#
#   Post:
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def number_to_letter(integer):
    letter_array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z']
    return letter_array[integer]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: letter_to_number(letter)
#
#   Pre:
#
#   Post:
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def letter_to_number(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return next((i for i, _letter in enumerate(alphabet) if _letter == letter), None)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: print_out_board(bool_player)
#
#   Pre:
#
#   Post:
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def print_out_board(board, bool_user):
    # cls() # Clear the screen TODO UN-COMMENT THIS WHEN FINISHED

    user = "User's " if bool_user else "Computer's "

    print(user + 'Board:\n     1     2     3     4     5     6     7     8     9     10\n')

    for i in range(len(board)):
        print(number_to_letter(i) + "  "),  # THIS COMMA IS NEEDED HERE TO NOT PRINT ON TO THE NEXT LINE!!!!
        for j in range(len(board)):
            if j < 9:
                print ' {:}  |'.format(board[i][j]),  # KEEP THIS COMMA!!!!
            else:
                print ' {:}'.format(board[i][j]),  # KEEP THIS COMMA!!!!
        if i < 9:
            print('\n   ------------------------------------------------------------')

    print '\n\n\n'


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Call to run the main program
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    random.seed(time.time())
    cls()
    main()
    raw_input('Press ENTER to continue...')
    cls()
