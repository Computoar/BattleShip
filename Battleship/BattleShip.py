import os
import re
import random
import time


# '''
# Program Prologue
# '''


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: main()
#
#   Pre: None.
#
#   Post: Runs the game.
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
#   Pre: None.
#
#   Post: Initializes two boards, user and computer. Runs the game. Prints out
#         the boards. Stops the game when either user or computer wins.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def run_game():
    # Initialize the board
    user_board = initialize_board(True)
    computer_board = initialize_board(False)

    # Initialize the ships each player has to start with.
    user_ships = {"A": 5, "B": 4, "S": 3, "D": 3, "P": 2}  # Ship list
    computer_ships = {"A": 5, "B": 4, "S": 3, "D": 3, "P": 2}  # Ship list

    # While the game is NOT over, continue playing the game.
    while True:
        cls()
        print_out_board(computer_board, False)
        make_move_user(computer_board)
        computer_ships = is_ship_sunken(computer_board, computer_ships)
        if is_game_over(computer_board):
            print 'GAME OVER! You won! WOOHOO!'
            break  # End the game, stop the while loop.
        raw_input('Press ENTER to continue...')

        cls()
        make_move_comp(user_board)
        raw_input('Press ENTER to continue...')
        user_ships = is_ship_sunken(user_board, user_ships)
        if is_game_over(user_board):
            print 'GAME OVER! Computer beat ya...'
            break  # End the game, stop the while loop.


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: initialize_board(bool_user)
#
#   Pre: Boolean for if we're deciding for the user input or not.
#
#   Post: Initializes the given boards based off of user input (always auto for
#         the computer).
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def initialize_board(bool_user):
    if bool_user:
        # Checks if the input is lowercase y
        if raw_input('Would you like to have your ships auto-deployed? y or n: ').lower() == "y":
            return auto_place_ships()  # Obviously yes, so auto-place ships.
        else:
            return manually_place_ships(True)  # Manually place them...false
    else:
        return auto_place_ships()  # Not the user, so auto-place them.


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: manually_place_ships(bool_user)
#
#   Pre: Boolean for if we're deciding for the user input or not.
#
#   Post: Initializes a new board (array), and loops through each and every ship
#         placing the ship at a specified user coordinate if possible. Returns
#         an initialized board with all pieces on the board.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def manually_place_ships(bool_user):
    board = ([[' ' for z in range(10)] for z in range(10)])  # Initialize board's slots to ' '. A 10x10 board is made.
    ships = {"Aircraft carrier": 5, "Battleship": 4, "Submarine": 3, "Destroyer": 3, "Patrol boat": 2}  # Ship list

    for ship in ships.keys():
        valid = False
        count = 0

        if bool_user:
            cls()
            print_out_board(board, bool_user)
            print "This is how your board looks.\n"

        while not valid:  # Loop through the validation, choosing random numbers till spot is found.
            if count == 0:
                placement = raw_input(
                    'Please enter your coordinate points for the ' + ship + ' (row, col, v/h): ').lower()
                count += 1  # Add 1 to the count
            else:
                placement = raw_input(
                    'Invalid placement, please try again for the ' + ship + ' (row, col, v/h): ').lower()

            position = placement.strip('()')  # Remove the '(' and ')' if the user entered them.
            position = position.replace(' ', '')  # Remove all blank space.
            position = position.split(",")  # Position is now an array of strings. Position is now an array.

            if len(position) != 3:
                print("Too few arguments." if len(position) < 3 else "Too many arguments.")
                continue

            if (position[2] != "v") and (position[2] != "h"):
                print("You did not select a 'v' or an 'h'.")
                continue

            if not represents_int(position[1]):
                print('Your column should be number.')
                continue

            if not represents_int(letter_to_number(position[0])):
                print('Your row should be a letter.')
                continue

            x = int(position[1]) - 1  # Assign x position
            y = letter_to_number(position[0])  # Assign y position
            o = 0 if position[2] == 'v' else 1  # Assign vertical/horizontal

            valid = can_place(board, ships[ship], y, x, o)  # Make sure we can place the ship there.

        board = place_ship(board, ships[ship], ship[0], y, x, o)  # We passed the tests, place the ship at that spot

    return board


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: auto_place_ships()
#
#   Pre: None.
#
#   Post: A board is initialized, and set with random ship placements, then returned.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def auto_place_ships():
    board = ([[' ' for z in range(10)] for z in range(10)])  # Initialize board's slots to ' '. A 10x10 board is made.
    ships = {"A": 5, "B": 4, "S": 3, "D": 3, "P": 2}  # Ship list

    for ship in ships.keys():
        valid = False
        while not valid:  # Loop through the validation, choosing random numbers till spot is found.
            y = random.randint(0, 9)  # Choose random number 0-9
            x = random.randint(0, 9)
            o = random.randint(0, 1)
            valid = can_place(board, ships[ship], y, x, o)  # Make sure we can place the ship there.
        board = place_ship(board, ships[ship], ship[0], y, x, o)  # We passed the tests, place the ship at that spot
    return board


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: can_place(board, ship, y, x, o)
#
#   Pre: The board, ship (length), y coordinate, x coordinate, and orientation
#        are passed in.
#
#   Post: Checks the board's positions at x and y to see if something is already
#         placed in that location.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def can_place(board, ship, y, x, o):
    if (o == 0 and y + ship > 10) or y < 0:  # Vertical
        return False
    elif (o == 1 and x + ship > 10) or x < 0:  # Horizontal
        return False
    else:
        if o == 0:  # Vertical
            for i in range(ship):
                if board[y + i][x] != ' ':
                    return False
        elif o == 1:  # Horizontal
            for i in range(ship):
                if board[y][x + i] != ' ':
                    return False

    return True


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: place_ship(board, ship, name, y, x, o)
#
#   Pre: The board, ship (length), name (character), y coordinate, x coordinate,
#        and orientation are passed in.
#
#   Post: The board's positions at the y and x coordinate are set equal to the
#         name, as well as the remainder of the length of the ship for it's
#         orientation.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def place_ship(board, ship, name, y, x, o):
    if o == 0:  # Vertical
        for i in range(ship):
            board[y + i][x] = name
    elif o == 1:  # Horizontal
        for i in range(ship):
            board[y][x + i] = name
    return board


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: make_move_user(board)
#
#   Pre:
#
#   Post:
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def make_move_user(board):
    ships = {"A": 5, "B": 4, "S": 3, "D": 3, "P": 2}  # Ship list
    count = 0

    while True:  # Loop through the validation, choosing random numbers till spot is found.
        if count == 0:
            placement = raw_input(
                'Please enter your coordinate points for your move (row, col): ').lower()
            count += 1  # Add 1 to the count
        else:
            placement = raw_input(
                'Invalid placement, please try again for the (row, col): ').lower()

        position = placement.strip('()')  # Remove the '(' and ')' if the user entered them.
        position = position.replace(' ', '')  # Remove all blank space.
        position = position.split(",")  # Position is now an array of strings. Position is now an array.

        if len(position) != 2:
            print("Too few arguments." if len(position) < 2 else "Too many arguments.")
            continue

        if not represents_int(position[1]):
            print('Your column should be number.')
            continue

        if not represents_int(letter_to_number(position[0])):
            print('Your row should be a letter.')
            continue

        x = int(position[1]) - 1  # Assign x position
        y = letter_to_number(position[0])  # Assign y position

        if y >= 10 or y < 0:
            print('Your column was too high. ' if y >= 10 else 'Your columns was too low.')
            continue

        if x >= 10 or x < 0:
            print('Your row was too high. ' if x >= 10 else 'Your row was too low.')
            continue

        if board[y][x] == '*' or board[y][x] == '$':  # If the spot is a hit or a miss
            print('You already chose this point.')  # Inform the user that they already used this point.
            continue

        if board[y][x] == ' ':  # The spot is empty
            board[y][x] = '*'  # Mark it as a miss
            cls()
            print_out_board(board, False)
            print('Miss!')
            break

        for ship in ships:
            if board[y][x] == ship:  # If the spot is a ship
                board[y][x] = '$'  # Mark it as a hit
                cls()
                print_out_board(board, False)
                print('HIT!!!!')
                break
        break


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: make_move_comp()
#
#   Pre:
#
#   Post:
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def make_move_comp(board):
    ships = {"A": 5, "B": 4, "S": 3, "D": 3, "P": 2}  # Ship list

    while True:  # Loop through the validation, choosing random numbers till spot is found.
        y = random.randint(0, 9)  # Choose random number 0-9
        x = random.randint(0, 9)

        if board[y][x] == '*' or board[y][x] == '$':
            continue

        if board[y][x] == ' ':
            board[y][x] = '*'
            cls()
            print_out_board(board, True)
            print('Computer misses at (' + number_to_letter(y) + ', ' + str(x+1) + ')!')
            break

        for ship in ships:
            if board[y][x] == ship:
                board[y][x] = '$'
                cls()
                print_out_board(board, True)
                print('Computer hit at (' + number_to_letter(y) + ', ' + str(x+1) + ')!')
                break
        break


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: is_ship_sunken()
#
#   Pre:
#
#   Post:
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def is_ship_sunken(board, ships):
    sunken_ship = 0
    for ship in ships:  # For every ship in the list (A, B, S, D, P)
        temp_counter = 0
        for x in range(len(board)):  # Go through the board right to left, up to down.
            for y in range(len(board)):
                if board[x][y] == ship:
                    temp_counter += 1
        if temp_counter == 0:
            print("Ship sunk: " + ship)
            sunken_ship = ship

    if sunken_ship in ships:  # Remove the ship from the list, so we don't display that we hit it again.
                del ships[sunken_ship]

    return ships  # Return the new array.


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: is_game_over()
#
#   Pre:
#
#   Post:
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def is_game_over(board):
    ships = {"A": 5, "B": 4, "S": 3, "D": 3, "P": 2}  # Ship list
    ships_left = 0
    for ship in ships:  # For every ship in the list (A, B, S, D)
        temp_counter = 0
        for x in range(len(board)):  # Go through the board right to left, up to down.
            for y in range(len(board)):
                if board[x][y] == ship:
                    temp_counter += 1
        if temp_counter > 0:  # There's 1 or more spots in the ship left to hit.
            ships_left += 1  # So, there is still a ship left.

    if ships_left == 0:  # If there are no more ships left, then the game is over.
        return True

    return False  # Game isn't over.


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: represents_int(string)
#
#   Pre: String (char) is passed in.
#
#   Post: Returns true if the character represents an integer or not. Does NOT
#         check for floating point numbers.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def represents_int(string):
    return (isinstance(string, int)) or (re.match(r"[-+]?\d+$", string) is not None)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: cls()
#   Pre: None.
#
#   Post: The console screen is cleared.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: number_to_letter(integer)
#
#   Pre: An integer is passed in.
#
#   Post: The letter at the integer's position in the array is returned i.e 0 = a.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def number_to_letter(integer):
    letter_array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z']
    return letter_array[integer]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: letter_to_number(letter)
#
#   Pre: A string letter is passed in.
#
#   Post: The letter is then checked through the array of chars (alphabet), and
#         returned as a character in that position i.e. a = 0, b = 1, c = 2. If
#         the character is not found in alphabet, None is returned.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def letter_to_number(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return next((i for i, _letter in enumerate(alphabet) if _letter == letter), None)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Function: print_out_board(board, bool_user)
#
#   Pre: An initialized board (array) is passed in.
#
#   Post: The board (array) is printed out to the console, showing all elements
#         in the array in a grid-like way.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def print_out_board(board, bool_user):
    # cls() # Clear the screen TODO UN-COMMENT THIS WHEN FINISHED

    user = "User's " if bool_user else "Computer's "  # Display board name.

    print(user + 'Board:\n     1     2     3     4     5     6     7     8     9     10\n')

    if not bool_user:  # Computer's board (only show hits/misses)
        for i in range(len(board)):
            print(number_to_letter(i) + "  "),  # THIS COMMA IS NEEDED HERE TO NOT PRINT ON TO THE NEXT LINE!!!!
            for j in range(len(board)):
                if j < 9:
                    if board[i][j] == "*" or board[i][j] == "$":
                        print ' {:}  |'.format(board[i][j]),  # KEEP THIS COMMA!!!!
                    else:
                        print '    |'.format(board[i][j]),  # KEEP THIS COMMA!!!!
                else:
                    if board[i][j] == "*" or board[i][j] == "$":
                        print ' {:}'.format(board[i][j]),  # KEEP THIS COMMA!!!!
                    else:
                        print '  '.format(board[i][j]),  # KEEP THIS COMMA!!!!
            if i < 9:
                print('\n   ------------------------------------------------------------')

    else:  # User's board (show everything)
        for i in range(len(board)):
            print(number_to_letter(i) + "  "),  # THIS COMMA IS NEEDED HERE TO NOT PRINT ON TO THE NEXT LINE!!!!
            for j in range(len(board)):
                if j < 9:
                    print ' {:}  |'.format(board[i][j]),  # KEEP THIS COMMA!!!!
                else:
                    print ' {:}'.format(board[i][j]),  # KEEP THIS COMMA!!!!
            if i < 9:
                print('\n   ------------------------------------------------------------')

    print '\n\n'


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
