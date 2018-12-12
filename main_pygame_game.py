import sys
import pygame
import pygame.draw
import scene as s
import menu as m
import time

grid_size = (10,30)
player_pos = (grid_size[0]/2,grid_size[1]-1)
barrier_h = 2
barrier_x_list = [(0,0),(3,5)]

__cellSize__ = 20

def start():
    sGame = s.GameScene(__cellSize__,grid_size,player_pos,barrier_h,barrier_x_list)
    sGame.loop()

def train():
    sTrain = s.TrainScene((300,200))
    sTrain.loop()

menu_list = [m.MenuItem("Start",1,start),m.MenuItem("Train",2,train)]

def main():
    menu = m.Menu(menu_list)
    menu.start_menu()
    # sTrain = s.TrainScene((300,200))
    # sTrain.loop()
    # sGame = s.GameScene(__cellSize__,grid_size,player_pos,barrier_h,barrier_x_list)
    # sGame.loop()
    pygame.quit()

main()
