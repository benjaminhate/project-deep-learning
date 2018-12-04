from brainAstar import BrainAstar as Brain
from moves import Moves as m
from unit import Unit

class Player(Unit):
    pos = (0,0)
    move_list = [m.RIGHT,m.LEFT,m.STILL]

    def __init__(self,pos):
        super(Player, self).__init__()
        self.brain = Brain()
        self.pos = pos

    def clone(self):
        player = Player(self.pos)
        return player

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

    def translate(self,trans):
        pos = list(self.pos)
        pos[0] += trans[0]
        pos[1] += trans[1]
        self.pos = tuple(pos)
