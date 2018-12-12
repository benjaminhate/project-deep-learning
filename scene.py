import pygame
from pygame import *
from game import Game
from grid import GridValue as gv
from brainNN import BrainNN
import time

class Scene:
    _mouseCoords = (0,0)
    _font = None
    _screenSize = None
    _done = False

    def __init__(self,screen_size):
        pygame.init()
        self._screen = pygame.display.set_mode(screen_size)
        self._font = pygame.font.SysFont('Arial',25)
        self._screenSize = screen_size

    def reset_screen(self):
        self._screen = pygame.display.set_mode(self._screenSize)

    def text_objects(self,text,font):
        textSurface = font.render(text,True,(0,0,0))
        return textSurface, textSurface.get_rect()

    def create_button(self,msg,x,y,w,h,ic,ac,action=None,args=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(self._screen, ac,(x,y,w,h))

            if click[0] == 1 and action != None:
                if args is None:
                    action()
                else:
                    action(args)
        else:
            pygame.draw.rect(self._screen, ic,(x,y,w,h))

        smallText = pygame.font.SysFont('Arial',20)
        textSurf, textRect = self.text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        self._screen.blit(textSurf, textRect)

    def drawMe(self):
        pass

    def drawText(self, text, position, color = (255,64,64)):
        self._screen.blit(self._font.render(text,1,color),position)

    def update(self):
        pass

    def loop(self):
        pass

class GameScene(Scene):
    _game = None
    _pause = False
    _cellSize = None

    __wallcolor = (10,10,10)
    __playercolor = (255,0,0)

    def getColorCell(self,n):
        if n == gv.WALL.value:
            return self.__wallcolor
        if n == gv.PLAYER.value:
            return self.__playercolor
        return (255,255,255)

    def __init__(self, cell_size, grid_size, player_pos, barrier_h, barrier_x_list):
        screen_size = tuple(map(lambda x: int(x*cell_size), grid_size))
        super(GameScene, self).__init__(screen_size)
        self._cellSize = cell_size
        self._game = Game.initialize(grid_size,player_pos,barrier_h,barrier_x_list,"model.h5")

    def drawMe(self):
        if self._game.grid is None:
            return
        self._screen.fill((128,128,128))
        for x in range(self._game.grid.size[0]):
            for y in range(self._game.grid.size[1]):
                pygame.draw.rect(self._screen,
                        self.getColorCell(self._game.grid.get(x,y)),
                        (x*self._cellSize + 1, y*self._cellSize + 1, self._cellSize-2, self._cellSize-2))

    def update(self):
        self._game.update()
        return self._game.check()

    def loop(self):
        clock = pygame.time.Clock()
        pause_time = 1
        start_time = time.time()
        while not self._done:
            clock.tick(20)
            if not self._pause and time.time() - start_time > pause_time:
                print("Update")
                start_time = time.time()
                self._done = self.update()
            self.drawMe()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Exiting")
                    self._done = True
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE: # q
                        print("Exiting")
                        self._done = True
                        break
                    if event.key == pygame.K_p:
                        print("Pause")
                        self._pause = not self._pause
                        break

class TrainScene(Scene):
    def __init__(self,screen_size):
        super(TrainScene, self).__init__(screen_size)

    def drawMe(self):
        self._screen.fill((200,200,200))

    def end(self):
        self._done = True

    def loop(self):
        self.drawMe()
        self.drawText("Training...",(10,10))
        pygame.display.flip()

        brain = BrainNN()
        neuronPerLayer = [3,2,2,2]
        brain.createNN(5,4,neuronPerLayer)
        brain.regenerateDb(1000)
        brain.trainNN(brain.database.data,brain.database.labels,20,2,1)
        brain.exportNN("model.h5")

        green = (0,255,0)
        bright_green = (100,255,100)

        self.drawText("Done !",(125,10))
        while not self._done:
            self.create_button("OK",self._screenSize[0]/2-50,self._screenSize[1]/2,100,50,green,bright_green,self.end)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Exiting")
                    self._done = True
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE: # q
                        print("Exiting")
                        self._done = True
                        break
            pygame.display.flip()
