from abstractBrain import AbstractBrain
from database import Database as db
import numpy as np
from keras.models import Sequential
from keras.layers import Dense,Dropout

class BrainNN(AbstractBrain):

    #The neural Network
    model = None
    database = None
    def __init__(self):
        self.model = Sequential()
        self.database = db(10)
        self.database.generateData()
        print(self.database.data)
        print(self.database.labels)

    def createNN(self,inputDim,layer,neuronPerLayer):
        #input dim      : the size of the input vector
        #layer          : the number of layer in the network
        #neuronPerLayer : a list of size hiden layer that contains the number of neurons per layer

        self.model.add(Dense(neuronPerLayer[0], input_dim = inputDim, kernel_initializer='uniform', activation='relu'))
        for i in range(1,layer):
            self.model.add(Dense(neuronPerLayer[i], kernel_initializer='uniform', activation='sigmoid'))
        
        # compile the model
        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        print(self.model.summary())

    def trainNN(self,data,labels,nbEpochs,batchSize,v=0):
        #training
        self.model.fit(data, labels, epochs=nbEpochs, batch_size=batchSize, verbose=v)

    def next_move(self,move_list):
        return move_list[0]
    
    def regenerateDb(self, nbVec):
        self.database = db(nbVec)
    