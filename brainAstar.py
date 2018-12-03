from abstractBrain import AbstractBrain


class BrainAstar(AbstractBrain):
    def __init__(self):
        self = self

    def next_move(self,move_list):
        return move_list[0]