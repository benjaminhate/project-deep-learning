from brainNN import BrainNN as Brain
from moves import Moves as m

class Barrier:
    b = None
    h = 0
    x_list = []
    move_list = [m.LEFT,m.RIGHT,m.STILL]
    last_move = None

    def __init__(self, h, x_list):
        self.b = Brain()
        self.h = h
        self.x_list = x_list

        #Creating the neural network
        neuronPerLayer = [1,2,2,2]
        self.b.createNN(5,4,neuronPerLayer)
        
        #Training the NN 
        #TODO add a method
        self.b.trainNN(self.b.database.data,self.b.database.labels,10,2,1)

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

    def update_x_list(self,trans):
        x_list = []
        for x in self.x_list:
            x = list(x)
            x[0] += trans
            x[1] += trans
            x_list.append(tuple(x))
        self.x_list = x_list

    def next_move(self,game):
        move_list = self.valid_move_list(game.grid.size)
        self.last_move = self.b.next_move(move_list)
        trans = self.last_move.translation()
        self.h += trans[1]
        self.update_x_list(trans[0])
