import sys
import pygame
import pygame.draw
from game import Game
from grid import GridValue as gv

grid_size = (10,30)
player_pos = (grid_size[0]/2,grid_size[1]-1)
barrier_h = 2
barrier_x_list = [(3,4)]

__cellSize__ = 20
__screenSize__ = tuple(map(lambda x: int(x*__cellSize__), grid_size))

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
    _game = None
    _font = None
    _process = None
    _end_process = 0

    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode(__screenSize__)
        self._font = pygame.font.SysFont('Arial',25)
        self._game = Game.initialize(grid_size,player_pos,barrier_h,barrier_x_list)

    def drawMe(self):
        if self._game.grid is None:
            return
        self._screen.fill((128,128,128))
        for x in range(self._game.grid.size[0]):
            for y in range(self._game.grid.size[1]):
                pygame.draw.rect(self._screen,
                        getColorCell(self._game.grid.grid.item((y,x))),
                        (x*__cellSize__ + 1, y*__cellSize__ + 1, __cellSize__-2, __cellSize__-2))

    def update(self):
        self._game.update()
        return self._game.check()

def main():
    print(__screenSize__)
    scene = Scene()
    done = False
    clock = pygame.time.Clock()
    while done == False:
        clock.tick(20)
        done = scene.update()
        scene.drawMe()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exiting")
                done=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key==pygame.K_ESCAPE: # q
                    print("Exiting")
                    done = True
                    break
        pygame.time.wait(1000)
    pygame.quit()

main()
