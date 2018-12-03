from brainAstar import BrainAstar as Brain
from moves import Moves as m

class Player:
    b = None
    pos = (0,0)
    move_list = [m.RIGHT,m.LEFT,m.STILL]
    last_move = None

    def __init__(self,pos):
        self.b = Brain()
        self.pos = pos

    def valid_move_list(self,grid_size):
        pos = list(self.pos)
        move_list = self.move_list.copy()
        if pos[0] == 0 and m.LEFT in move_list:
            move_list.remove(m.LEFT)
        if pos[0] == grid_size[0] - 1 and m.RIGHT in move_list:
            move_list.remove(m.RIGHT)
        if pos[1] == 0 and m.UP in move_list:
            move_list.remove(m.UP)
        if pos[1] == grid_size[1] - 1 and m.DOWN in move_list:
            move_list.remove(m.DOWN)
        return move_list

    def next_move(self,game):
        pos = list(self.pos)
        move_list = self.valid_move_list(game.grid.size)
        self.last_move = self.b.next_move(move_list)
        trans = self.last_move.translation()
        pos[0] += trans[0]
        pos[1] += trans[1]
        self.pos = tuple(pos)
