from abstractBrain import AbstractBrain
from database import Database as db
import numpy as np
from keras.models import Sequential
from keras.layers import Dense,Dropout
from keras.models import load_model

from moves import Moves

class BrainNN(AbstractBrain):

    #The neural Network
    model = None
    database = None
    def __init__(self):
        self.model = Sequential()
        self.database = db(10)
        self.database.generateData()
        #print(self.database.data)
        #print(self.database.labels)

    def createNN(self,inputDim,layer,neuronPerLayer):
        #input dim      : the size of the input vector
        #layer          : the number of layer in the network
        #neuronPerLayer : a list of size hiden layer that contains the number of neurons per layer

        self.model.add(Dense(neuronPerLayer[0], input_dim = inputDim, kernel_initializer='uniform', activation='relu'))
        for i in range(1,layer):
            self.model.add(Dense(neuronPerLayer[i], kernel_initializer='uniform', activation='sigmoid'))

        # compile the model
        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        #print(self.model.summary())

    def trainNN(self,data,labels,nbEpochs,batchSize,v=0):
        #training
        #self.model.fit(data, labels, epochs=nbEpochs, batch_size=batchSize, verbose=v)

        #in case you want to export the model
        # self.exportNN("model.h5")

        #import a model instead of training
        self.importNN("model.h5")


    def next_move(self,move_list,game):
        player_pos = list(game.player.pos)
        barrier_x_list = list(game.barrier.x_list[0])
        barrier_h = game.barrier.h
        size = list(game.grid.size)
        data = []
        xp = player_pos[0]/size[0]
        yp = player_pos[1]/size[1]
        h = barrier_h/size[1]
        xd = barrier_x_list[0]/size[0]
        xf = barrier_x_list[1]/size[0]

        vec = np.array([xp, yp, h, xd, xf])
        data.append(vec)

        data = np.array(data)
        pred = self.model.predict(data)
        pred = pred > 0.5
        #print(pred)
        if pred[0][0] == True:
            #go right
            move = Moves.RIGHT
        else:
            #go left
            move = Moves.LEFT

        if move in move_list:
            return move

        return Moves.STILL

    def regenerateDb(self, nbVec):
        self.database = db(nbVec)
        self.database.generateData()

    def exportNN(self,name):
        self.model.save(name)

    def importNN(self,name):
        self.model = load_model(name)
