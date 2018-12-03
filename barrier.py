from brainNN import BrainNN as Brain
from moves import Moves as m
from unit import Unit

class Barrier(Unit):
    h = 0
    x_list = []
    move_list = [m.LEFT,m.RIGHT,m.STILL]

    def __init__(self, h, x_list):
        super(Barrier, self).__init__()
        self.brain = Brain()
        self.h = h
        self.x_list = x_list

        #Creating the neural network
        neuronPerLayer = [1,2,2,2]
        self.brain.createNN(5,4,neuronPerLayer)
        
        #Training the NN 
        #TODO add a method
        self.brain.regenerateDb(1000)
        self.brain.trainNN(self.brain.database.data,self.brain.database.labels,15,2,1)

    def valid_move_list(self,grid_size):
        move_list = self.move_list.copy()
        if max(max(self.x_list)) == grid_size[0] - 1 and m.RIGHT in move_list:
            move_list.remove(m.RIGHT)
        if min(min(self.x_list)) == 0 and m.LEFT in move_list:
            move_list.remove(m.LEFT)
        if self.h == 0 and m.UP in move_list:
            move_list.remove(m.UP)
        if self.h == grid_size[1] - 1 and m.DOWN in move_list:
            move_list.remove(m.DOWN)
        return move_list

    def translate(self,trans):
        self.h += trans[1]
        x_list = []
        for x in self.x_list:
            x = list(x)
            x[0] += trans[0]
            x[1] += trans[0]
            x_list.append(tuple(x))
        self.x_list = x_list
