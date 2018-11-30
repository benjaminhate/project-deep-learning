from player import Player
from barrier import Barrier
import numpy as np

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
        self.barrier = Barrier(2,[(2,2)])
        self.update_grid()

    def update(self):
        self.player.next_move()
        self.barrier.next_move()
        self.update_grid()

    def update_grid(self):
        for x in range(self.grid.size[0]):
            for y in range(self.grid.size[1]):
                self.grid.grid[y,x] = 0
                if (x,y) == self.player.pos:
                    self.grid.grid[y,x] = 1
                if y == self.barrier.h and (x<self.barrier.x_list[0][0] or x>self.barrier.x_list[0][1]):
                    self.grid.grid[y,x] = 2

    def draw(self):
        print(self.grid.grid)

game = Game()
game.draw()
for i in range(5):
    game.update()
    game.draw()
