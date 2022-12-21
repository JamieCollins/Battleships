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

ocean_grid = [["O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O"]]


import random

def play_game():
    """
    Creates the "ocean" from a 2D grid of 5x5 rows and colummns.
    """

    ship_1 = ship_point_randomiser()
    ship_2 = ship_point_randomiser()
    ship_3 = ship_point_randomiser()

    print(ship_1)
    print(ship_2)
    print(ship_3)

    grid_print()

    #Asks user to pick two numbers, checks if numbers hit a ships location.

    row = int(input("Choose a number between 0 and 4: "))
    col = int(input("Choose a number between 0 and 4: "))
    if (row, col) == ship_1 or (row, col) == ship_2 or (row, col) == ship_3:
        print("Success")
        ocean_grid[row][col] = "X"
        grid_print()
    else:
        print("Missed")
        ocean_grid[row][col] = "."
        grid_print()

def grid_print():
    for i in ocean_grid:
        print(*i)
    

def ship_point_randomiser():
    """
    Creates points for ships to be placed.
    """
    return random.randint(0, 4), random.randint(0, 4)


play_game()