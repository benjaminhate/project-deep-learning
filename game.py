from player import Player
from barrier import Barrier
import numpy as np
from enum import Enum
import copy

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

class Game:
    player = None
    barrier = None
    grid = None

    def __init__(self):
        self.grid = Grid((5,5))
        self.player = Player((0,0))
        self.barrier = Barrier(2,[(3,4)])
        self.update_grid()

    def update(self):
        # Saving the game status to not influence the barrier from the player's next move
        game = copy.deepcopy(self)
        self.player.next_move(game)
        self.barrier.next_move(game)
        self.update_grid()

    def update_grid(self):
        for x in range(self.grid.size[0]):
            for y in range(self.grid.size[1]):
                self.grid.grid[y,x] = GridValue.EMPTY.value
                if (x,y) == self.player.pos:
                    self.grid.grid[y,x] = GridValue.PLAYER.value
                if y == self.barrier.h:
                    for xs in self.barrier.x_list:
                        if x >= xs[0] and x <= xs[1]:
                            self.grid.grid[y,x] = GridValue.HOLE.value
                        elif self.grid.grid[y,x] != GridValue.HOLE.value:
                            self.grid.grid[y,x] = GridValue.WALL.value

    def draw(self):
        print(self.grid.grid)

game = Game()
game.draw()
for i in range(5):
    game.update()
    game.draw()
