from enum import Enum

class Moves(Enum):
    STILL = 0
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4

    def translation(self):
        trans = [0,0]
        if(self == Moves.LEFT):
            trans[0] = -1
        if(self == Moves.RIGHT):
            trans[0] = 1
        if(self == Moves.UP):
            trans[1] = -1
        if(self == Moves.DOWN):
            trans[1] = 1
        return tuple(trans)

    def from_translation(trans):
        if(Moves.LEFT.translation() == trans):
            return Moves.LEFT
        if(Moves.RIGHT.translation() == trans):
            return Moves.RIGHT
        if(Moves.UP.translation() == trans):
            return Moves.UP
        if(Moves.DOWN.translation() == trans):
            return Moves.DOWN
        return Moves.STILL
