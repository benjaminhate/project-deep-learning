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

#x_max = grid_size[0] and y_max = grid_size[1]
grid_size = (10,15)
player_pos = (grid_size[0]/2,grid_size[1]-1)
barrier_h = 2
barrier_x_list = [(3,4)]

game = Game(grid_size,player_pos,barrier_h,barrier_x_list)
game.draw()
while(not game.check()):
    game.update()
    game.draw()
