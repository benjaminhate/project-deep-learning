import pygame
from game import Game
from grid import GridValue as gv

__wallcolor = (10,10,10)
__playercolor = (255,0,0)

def getColorCell(n):
    if n == gv.WALL.value:
        return __wallcolor
    if n == gv.PLAYER.value:
        return __playercolor
    return (255,255,255)

class Scene:
    _mouseCoords = (0,0)
    _font = None
    _screenSize = None

    def __init__(self,screen_size):
        pygame.init()
        self._screen = pygame.display.set_mode(screen_size)
        self._font = pygame.font.SysFont('Arial',25)
        self._screenSize = screen_size

    def drawMe(self):
        pass

    def update(self):
        pass

    def events(self):
        pass

class GameScene(Scene):
    _game = None
    _pause = False
    _cellSize = None

    def __init__(self, cell_size, grid_size, player_pos, barrier_h, barrier_x_list):
        screen_size = tuple(map(lambda x: int(x*cell_size), grid_size))
        super(GameScene, self).__init__(screen_size)
        self._cellSize = cell_size
        self._game = Game.initialize(grid_size,player_pos,barrier_h,barrier_x_list)

    def drawMe(self):
        if self._game.grid is None:
            return
        self._screen.fill((128,128,128))
        for x in range(self._game.grid.size[0]):
            for y in range(self._game.grid.size[1]):
                pygame.draw.rect(self._screen,
                        getColorCell(self._game.grid.get(x,y)),
                        (x*self._cellSize + 1, y*self._cellSize + 1, self._cellSize-2, self._cellSize-2))

    def update(self):
        self._game.update()
        return self._game.check()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exiting")
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key==pygame.K_ESCAPE: # q
                    print("Exiting")
                    return True
                    break
                if event.key == pygame.K_p:
                    print("Pause")
                    self._pause = not self._pause
                    break
        return False
