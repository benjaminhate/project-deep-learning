from brainNN import BrainNN as Brain
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
        
        #Creating the neural network
        neuronPerLayer = [1,2,2,1]
        self.b.createNN(4,4,neuronPerLayer)

    def next_move(self,game):
        self.b.next_move(self.move_list)
