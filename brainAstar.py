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
        node_list = []

        start = a.node((player_pos[0],player_pos[1],a.nodeState.START))
        start.boundary = True
        final = a.node((2,0,a.nodeState.FINAL))
        final.f = math.inf

        node_list.append(start)
        node_list.append(final)

        #TODO A OPTIMISER !
        for x in range(game.grid.size[0]):
            for y in range(game.grid.size[1]):
                if game.grid.grid[y,x] == gv.WALL.value:
                    n = a.node((x,y,a.nodeState.WALL,1))
                    node_list.append(n)

        path = a.astar(node_list,start,final,game.grid.size)
        while path.father and path.father.state[2] != a.nodeState.START:
            path = path.father

        if path is not None:
            player_next_pos = list(path.get_pos())
            player_last_pos = list(player_pos)
            trans = [player_next_pos[0] - player_last_pos[0],player_next_pos[1]-player_last_pos[1]]
            move = Moves.from_translation(tuple(trans))
            if move in move_list:
                return move

        return Moves.STILL
