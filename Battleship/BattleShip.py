import os
import random
import time

__author__ = 'Emma & Lee'

# '''
# Program Prologue
# '''


# Create 2 global lists for our boards.
board_array_user = [[' ' for z in range(10)] for z in range(10)]
board_array_computer = [[' ' for z in range(10)] for z in range(10)]
ship_list_user = ['AAAAA', 'BBBB', 'SSS', 'PP']
ship_list_computer = ['AAAAA', 'BBBB', 'SSS', 'PP']


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
    initialize_board()

    # While the game is NOT over, continue playing the game.
    while not is_game_over():
        print_out_board(True)
        make_move_user()
        is_ship_sunken()
        if is_game_over():
            print 'game over! You won! WOOHOO!'

        print_out_board(True)
        make_move_comp()
        is_ship_sunken()
        if is_game_over():
            print 'game over! Computer beat ya...'


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: initialize_board()
#
#   Pre:
#
#   Post:
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def initialize_board():
    # Place the computer's ships.
    # auto_place_ships()

    # Checks if the input is lowercase y
    if raw_input('Would you like to have your ships auto-deployed? y or n: ').lower() == "y":
        # Obviously yes, so auto-place ships.
        auto_place_ships()
    else:
        # Manually place them...false
        manually_place_ships()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: print_out_board(bool_player)
#
#   Pre:
#
#   Post:
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def print_out_board(bool_player):
    # Clear the screen
    # cls() TODO UN-COMMENT THIS WHEN FINISHED

    print('User\'s Board:\n     1     2     3     4     5     6     7     8     9     10\n')

    # Ternary operator which decides which board to display. True = Player, False = Computer
    board = board_array_user if bool_player else board_array_computer

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
#   Function: number_to_letter(int)
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
#   Function: auto_place_ships(list)
#
#   Pre:
#
#   Post:
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def auto_place_ships(bool_user):
    place = True
    board = board_array_user if bool_user else board_array_computer
    ship_list = ship_list_user if bool_user else ship_list_computer
    while place:
        x = random.randint(1, 10) - 1
        y = random.randint(1, 10) - 1
        orientation = random.randint(0, 1)

        for i in range(ship_list):  # For each of the ships in the list...  ['AAAAA', 'BBBB', 'SSS', 'PP']
            if orientation == 1:  # Vertical orientation
                for j in range(ship_list[i]):  # For one particular ship 'AAAAA'
                    while (x + j) < 10:
                        x = random.randint(1, 10) - 1  # Check to make sure the ship won't go off the board.
                    board[x + j][y] = ship_list[j]  # The board's info @ x + j = the letter of the particular ship
                    x = random.randint(1, 10) - 1  # New coordinate point for next ship assigned.
                    y = random.randint(1, 10) - 1  # New coordinate point for next ship assigned.
                    orientation = random.randint(0, 1)  # New rotation for next ship assigned.
            else:
                for i in range(ship_list):  # For each of the ships in the list...  ['AAAAA', 'BBBB', 'SSS', 'PP']
                    for j in range(ship_list[i]):  # For one particular ship 'AAAAA'
                        while (y + j) < 10:
                            y = random.randint(1, 10) - 1  # Check to make sure the ship won't go off the board.
                        board[x][y + j] = ship_list[j]  # The board's info @ x + j = the letter of the particular ship
                        x = random.randint(1, 10) - 1  # New coordinate point for next ship assigned.
                        y = random.randint(1, 10) - 1  # New coordinate point for next ship assigned.
                        orientation = random.randint(0, 1)  # New rotation for next ship assigned.


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: manually_place_ships(col, row, pos, list)
#
#   Pre:
#
#   Post:
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def manually_place_ships(col, row, pos, list):
    print 'Manually place'


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
#   Function: cls(#)
#   Pre:
#
#   Post:
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


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
