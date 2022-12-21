"""
-A simple battleships game.
-The ocean for the ships is created on a grid of 5 rows and 5 columns
totalling 25 points.
-Each point on the grid that symbolises the ocean is created with a "0".
-3 ships of length 3 points are placed randomly.
-The game will verify that the ships are correctly placed on grid and not
overlapping.
-The user gets a turn to try and hit the opponents ship by shooting at one
point.
-Feedback is returned to the user after each turn stating if they have hit the
ship or missed the ship.
-If they have given an invalid point which is not on the grid, or if they
given a point on the grid they have already chosen,
they will be given feedback and prompted to try again.
-The game continues until all 3 ships are completely hit.
"""

import random

def create_grid():
    """
    Creates the "ocean" from a 2D grid of 5x5 rows and colummns.
    """

    ocean_grid = [["O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O"]]

    for i in ocean_grid:
        print(*i)


create_grid()