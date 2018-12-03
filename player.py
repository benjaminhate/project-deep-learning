from brainAstar import BrainAstar as Brain
from moves import Moves as m

class Player:
    b = None
    pos = (0,0)
    move_list = [m.RIGHT,m.LEFT,m.UP,m.STILL]

    def __init__(self,pos):
        self.b = Brain()
        self.pos = pos

    def next_move(self):
        trans = self.b.next_move(self.move_list).translation()
        pos = list(self.pos)
        pos[0] += trans[0]
        pos[1] += trans[1]
        self.pos = tuple(pos)
