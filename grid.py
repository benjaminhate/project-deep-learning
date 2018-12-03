from enum import Enum
import numpy as np

class GridValue(Enum):
    EMPTY = 0
    PLAYER = 1
    WALL = 2
    HOLE = 3
    FINAL = 4

class Grid:
    size = (0,0)
    grid = None

    def __init__(self,size):
        print("Creating a grid of dimensions " + str(size))
        self.size = size
        self.grid = np.zeros(size)
