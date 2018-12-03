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
    win = None

    def __init__(self,grid_size,player_pos,barrier_h,barrier_x_list):
        self.grid = Grid(grid_size)
        self.player = Player(player_pos)
        self.barrier = Barrier(barrier_h,barrier_x_list)
        self.update_grid()

    def update(self):
        # Saving the game status to not influence the barrier from the player's next move
        game = copy.deepcopy(self)
        self.player.next_move(game)
        self.barrier.next_move(game)
        self.force_move()
        self.update_grid()

    def force_move(self):
        self.player.translate((0,-1))

    def check(self):
        if(self.player.pos[1] == 0):
            print("PLAYER WIN")
            self.win = True
            return True
        return False

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

grid_size = (5,5)
player_pos = (0,4)
barrier_h = 2
barrier_x_list = [(2,2)]

game = Game(grid_size,player_pos,barrier_h,barrier_x_list)
game.draw()
while(not game.check()):
    game.update()
    game.draw()
