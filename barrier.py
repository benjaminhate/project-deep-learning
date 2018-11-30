from brain import Brain
from moves import Moves as m

class Barrier:
    b = None
    h = 0
    x_list = []
    move_list = [m.LEFT,m.RIGHT,m.STILL]

    def __init__(self, h, x_list):
        self.b = Brain()
        self.h = h
        self.x_list = x_list

    def next_move(self):
        self.b.next_move(self.move_list)
