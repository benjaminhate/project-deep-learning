import pygame
from pygame import *
import scene as s

class MenuItem:
    _name = None
    _value = None
    _callback = None

    def __init__(self,name,value,callback):
        self._name = name
        self._value = value
        self._callback = callback

class Menu:
    _menu_list = []
    _menu_scene = None

    def __init__(self,menu_list):
        self._menu_list = menu_list
        self._screenSize = (300,(len(self._menu_list))*100)
        self._menu_scene = MenuScene(self._screenSize,self._menu_list)

    def detection(self):
        for item in self._menu_list:
            if self._menu_scene._end_value == item._value:
                self._menu_scene.reset()
                item._callback()

    def start_menu(self):
        while not self._menu_scene._done:
            self._menu_scene.reset()
            self._menu_scene.reset_screen()
            self._menu_scene.loop()
            self.detection()

class MenuScene(s.Scene):
    _end_value = -1
    _menu_list = []

    def __init__(self,screen_size,menu_list):
        super(MenuScene, self).__init__(screen_size)
        self._menu_list = menu_list

    def drawMe(self):
        self._screen.fill((200,200,200))

    def end_value(self,value):
        self._end_value = value
        self._done = True

    def reset(self):
        self._end_value = -1
        self._done = False

    def create_menu_buttons(self):
        green = (0,255,0)
        bright_green = (50,255,50)

        w = 100
        h = 50

        for i in range(len(self._menu_list)):
            item = self._menu_list[i]
            self.create_button(item._name,self._screenSize[0]/2-(w/2),10+(h*2)*i,w,h,green,bright_green,self.end_value,item._value)

    def loop(self):
        self.drawMe()
        while not self._done:
            self.create_menu_buttons()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Exiting")
                    self._done = True
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        print("Exiting")
                        self._done = True
                        break
            pygame.display.flip()
