"""
-A simple battleships game.
-The ocean for the ships is created on a grid of 5 rows and 5 columns
totalling 25 points.
-Each point on the grid that symbolises the ocean is created with a "0".
-3 ships are placed randomly.
-The game will verify that the ships are correctly placed on grid.
-The user gets a turn to try and hit the ships by shooting at one point.
-Feedback is returned to the user after each turn stating if they have hit the
ship or missed the ship.
-If they have given an invalid point which is not on the grid, or if they
given a point on the grid they have already chosen,
they will be given feedback and prompted to try again.
-The game continues until all 3 ships are completely hit.
"""


import random


"""
Creates the "ocean" from a 2D grid of 5x5 rows and colummns.
"""
ocean_grid = [["O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O"]]


def play_game():
    """
    The main code that runs the game.
    """
    ship_counter = 3
    shots_taken = 0
    ship_1 = ship_point_randomiser()
    ship_2 = ship_point_randomiser()
    ship_3 = ship_point_randomiser()

    print(ship_1)
    print(ship_2)
    print(ship_3)

    grid_print()


    """
    Asks user to pick two numbers, 
    checks if numbers hit a ships location,
    updates grid display showing 'hits' and 'misses'.
    """
    while ship_counter > 0:
        row = int(input("Choose a number between 1 and 5: "))
        col = int(input("Choose a number between 1 and 5: "))


        if (row - 1, col - 1) == ship_1 or (row - 1, col - 1) == ship_2 or (row - 1, col - 1) == ship_3:
            print("Success, you hit a ship!")
            ocean_grid[row - 1][col - 1] = "X"
            ship_counter = ship_counter - 1
            shots_taken = shots_taken + 1
            grid_print()
        else:
            print("You missed, try again!")
            ocean_grid[row - 1][col - 1] = "."
            shots_taken = shots_taken + 1
            grid_print()

    if ship_counter == 0:
        print(f"Congratulations you shunk all the ships. You took {shots_taken} shots to win!")


def grid_print():
    """
    Prints the grid for the game when called.
    """
    for i in ocean_grid:
        print(*i)
    

def ship_point_randomiser():
    """
    Assigns random rows and columns to ships within grid range
    """
    return random.randint(0, 4), random.randint(0, 4)


play_game()