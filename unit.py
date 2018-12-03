class Unit:
    brain = None
    move_list = []
    last_move = None

    def __init__(self):
        pass

    def valid_move_list(self,grid_size):
        return self.move_list

    def translate(self,trans):
        pass

    def next_move(self,game):
        move_list = self.valid_move_list(game.grid.size)
        self.last_move = self.brain.next_move(move_list,game)
        trans = self.last_move.translation()
        self.translate(trans)
