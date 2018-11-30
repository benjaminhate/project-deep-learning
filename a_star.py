import math
from enum import Enum

class nodeState(Enum):
    EMPTY = 0
    WALL = 1
    START = 2
    FINAL = 3
    SEARCH = 4
    PATH = 5

class node:
    father = 0
    state = 0
    dejaVu = False
    boundary = False
    g = 0
    f = 0

    def __init__(self,state):
        self.state = state

    def __str__(self):
        father =  "False" if self.father == 0 else str(self.father.state)
        return "Node "+str(self.state)+" "+str(self.boundary)+" "+str(self.dejaVu)+" Father "+father

    def h(self,final):
        return abs(self.state[0] - final.state[0]) + abs(self.state[1] - final.state[1])

    def cost(self):
        if(self.state[2] == nodeState.WALL):
            return self.state[3] * 100
        else:
            return 1

def cost(n1,n2):
    return n1.cost() + n2.cost()

def frontier_empty(node_list):
    for n in node_list:
        if n.boundary:
            return False
    return True

def frontier_choose(node_list):
    choice = node((0,0,nodeState.EMPTY))
    choice.f = math.inf
    for n in node_list:
        if n.boundary and n.f < choice.f:
            choice = n
    return choice

def getNode(node_list, state):
    for n in node_list:
        if n.state[0] == state[0] and n.state[1] == state[1]:
            return n
    return False

def successor(node_list, n, maxX, maxY):
    s_list = []
    x = n.state[0]
    y = n.state[1]
    s1 = getNode(node_list, (x+1,y))
    s2 = getNode(node_list, (x-1,y))
    s3 = getNode(node_list, (x,y+1))
    s4 = getNode(node_list, (x,y-1))
    if not s1 and x+1 < maxX:
        s1 = node((x+1,y,nodeState.SEARCH))
    if s1:
        s_list.append(s1)
    if not s2 and x-1 > 0:
        s2 = node((x-1,y,nodeState.SEARCH))
    if s2:
        s_list.append(s2)
    if not s3 and y+1 < maxY:
        s3 = node((x,y+1,nodeState.SEARCH))
    if s3:
        s_list.append(s3)
    if not s4 and y-1 > 0:
        s4 = node((x,y-1,nodeState.SEARCH))
    if s4:
        s_list.append(s4)
    return s_list

def equals(n1,n2):
    return n1.state[0] == n2.state[0] and n1.state[1] == n2.state[1]

def astar(node_list, start, final, grid_size):
    success = False
    while(not frontier_empty(node_list) and not success):
        n = frontier_choose(node_list)
        if equals(n,final):
            success = True
            return n
        else:
            n.boundary = False
            n.dejaVu = True
            for s in successor(node_list, n, grid_size[0], grid_size[1]):
                if not s.boundary and not s.dejaVu:
                    s.father = n
                    s.g = n.g + cost(n,s)
                    s.f = s.g + s.h(final)
                    s.boundary = True
                else:
                    if s.g > n.g + cost(n,s):
                        if s.dejaVu:
                            s.dejaVu = False
                        s.father = n
                        s.g = n.g + cost(n,s)
                        s.f = s.g + s.h(final)
                        s.boundary = True
                node_list.append(s)
    return False
