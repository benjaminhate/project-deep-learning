from player import Player
from barrier import Barrier
import copy
import grid as g

class Game:
    player = None
    barrier = None
    grid = None
    win = None

    def __init__(self,grid_size,player_pos,barrier_h,barrier_x_list):
        self.grid = g.Grid(grid_size)
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
        for x in range(self.grid.size[0]):
            for y in range(self.grid.size[1]):
                self.grid.grid[y,x] = g.GridValue.EMPTY.value
                if y == self.barrier.h:
                    for xs in self.barrier.x_list:
                        if x >= xs[0] and x <= xs[1]:
                            self.grid.grid[y,x] = g.GridValue.HOLE.value
                        elif self.grid.grid[y,x] != g.GridValue.HOLE.value:
                            self.grid.grid[y,x] = g.GridValue.WALL.value
                if (x,y) == self.player.pos:
                    self.grid.grid[y,x] = g.GridValue.PLAYER.value

    def draw(self):
        print(self.grid.grid)

grid_size = (10,10)
player_pos = (0,9)
barrier_h = 2
barrier_x_list = [(3,4)]

game = Game(grid_size,player_pos,barrier_h,barrier_x_list)
game.draw()
while(not game.check()):
    game.update()
    game.draw()
