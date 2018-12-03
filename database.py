#The point of this class is to generate data to train the neural network
import numpy as np
import random



class Database:
    data = None
    labels = None
    nbVec = None

    def __init__(self,nbVec):
        self.data = np.zeros(nbVec)
        self.labels = np.zeros(nbVec)
        self.nbVec = nbVec
    
    def h1(self,yp,xp,h,xd,xf):
        return abs(yp-h)*(abs((xp + 1) - xd) + abs((xp + 1) - xf))
    
    def h2(self,yp,xp,h,xd,xf):
        return abs(yp-h)*(abs((xp - 1) - xd) + abs((xp - 1) - xf))

    def heuristic(self,yp,xp,h,xd,xf):
        h = self.h1(yp,xp,h,xd,xf) - self.h2(yp,xp,h,xd,xf)

        if(h > 0):
            #go right
            return np.array([1,0])
        else:
            #go left
            return np.array([0,1])


    def generateData(self):
        data = []
        labels = []
        for i in range(self.nbVec):
            xp = random.uniform(0, 1)
            yp = random.uniform(0, 1)
            h = random.uniform(0, 1)
            xd = random.uniform(0, 1)
            xf = random.uniform(0, 1)
            l = [xp, yp, h, xd, xf]
            data.append(np.array(l))
            labels.append(self.heuristic(yp,xp,h,xd,xf))
        self.data = np.array(data)
        self.labels = np.array(labels)

