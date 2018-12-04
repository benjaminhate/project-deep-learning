from player import Player
from barrier import Barrier
import copy
import grid as g
import time

class Game:
    player = None
    barrier = None
    grid = None
    win = None

    def __init__(self):
        pass

    def initialize(grid_size,player_pos,barrier_h,barrier_x_list):
        game = Game()
        game.grid = g.Grid(grid_size)
        game.player = Player(player_pos)
        game.barrier = Barrier(barrier_h,barrier_x_list)
        game.barrier.createNN()
        game.barrier.train()
        game.update_grid()
        return game

    def clone(self):
        game = Game()
        game.player = self.player.clone()
        game.barrier = self.barrier.clone()
        game.grid = self.grid.clone()
        game.update_grid()
        return game

    def update(self):
        # Saving the game status to not influence the barrier from the player's next move
        start_time = time.time()
        game = self.clone()
        print("------------ DEEPCOPY time : %s seconds" % (time.time() - start_time))
        start_time = time.time()
        self.player.next_move(game)
        print("------------ PLAYER time : %s seconds" % (time.time() - start_time))
        start_time = time.time()
        self.barrier.next_move(game)
        print("------------ BARRIER time : %s seconds" % (time.time() - start_time))
        start_time = time.time()
        self.force_move()
        print("------------ FORCE MOVE time : %s seconds" % (time.time() - start_time))
        start_time = time.time()
        self.update_grid()
        print("------------ UPDATE time : %s seconds" % (time.time() - start_time))

    def force_move(self):
        self.player.translate((0,-1))

    def check(self):
        if self.player.pos[1] == 0:
            print("PLAYER WIN")
            self.win = True
            return True
        if self.player.pos[1] == self.barrier.h:
            px = self.player.pos[0]
            for x in self.barrier.x_list:
                if px < x[0] or px > x[1]:
                    print("PLAYER LOOSE")
                    self.win = False
                    return True
        return False

    def update_grid(self):
        wall_x = self.barrier.get_wall_x(self.grid.size)
        for j in range(self.grid.size[1]):
            for i in range(self.grid.size[0]):
                self.grid.grid[j,i] = g.GridValue.EMPTY.value
                if j == self.barrier.h:
                    if i in wall_x:
                        self.grid.grid[j,i] = g.GridValue.WALL.value
                    else:
                        self.grid.grid[j,i] = g.GridValue.HOLE.value
                if (i,j) == self.player.pos:
                    self.grid.grid[j,i] = g.GridValue.PLAYER.value

    def draw(self):
        print(self.grid.grid)
