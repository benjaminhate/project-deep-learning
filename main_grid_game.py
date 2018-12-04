from game import Game
import time

#x_max = grid_size[0] and y_max = grid_size[1]
grid_size = (10,15)
player_pos = (grid_size[0]/2,grid_size[1]-1)
barrier_h = 2
barrier_x_list = [(3,4)]

game = Game.initialize(grid_size,player_pos,barrier_h,barrier_x_list)
game.draw()
while(not game.check()):
    game.update()
    game.draw()
    time.sleep(1)
