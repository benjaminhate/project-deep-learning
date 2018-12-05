from abstractBrain import AbstractBrain
import a_star as a
import math
from grid import GridValue as gv
from moves import Moves

class BrainAstar(AbstractBrain):
    def __init__(self):
        self = self

    def next_move(self,move_list,game):
        player_pos = game.player.pos
        move_prob = []

        for i in range(game.grid.size[0]):
            node_list = []

            start = a.node((player_pos[0],player_pos[1],a.nodeState.START))
            start.boundary = True
            final = a.node((i,0,a.nodeState.FINAL))
            final.f = math.inf

            node_list.append(start)
            node_list.append(final)

            y = game.barrier.h
            for x in game.barrier.get_wall_x(game.grid.size):
                n = a.node((x,y,a.nodeState.WALL,1))
                node_list.append(n)

            path = a.astar(node_list,start,final,game.grid.size)
            if path:
                while path.father and path.father.state[2] != a.nodeState.START:
                    path = path.father
                if path is not None:
                    player_next_pos = list(path.get_pos())
                    player_last_pos = list(player_pos)
                    trans = [player_next_pos[0] - player_last_pos[0],player_next_pos[1]-player_last_pos[1]]
                    move = Moves.from_translation(tuple(trans))
                    if move in move_list:
                        move_prob.append(move)

        s = [0,0]
        for move in move_prob:
            print(move)
            t = list(move.translation())
            s[0] += t[0]
            s[1] += t[1]
        if s[0] > 0:
            s[0] = 1
        elif s[0] < 0:
            s[0] = -1
        if s[1] > 0:
            s[1] = 1
        elif s[1] < 0:
            s[1] = -1
        print(s)
        return Moves.from_translation(tuple(s))
