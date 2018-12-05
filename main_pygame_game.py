import sys
import pygame
import pygame.draw
import scene as s
import time

grid_size = (10,30)
player_pos = (grid_size[0]/2,grid_size[1]-1)
barrier_h = 2
barrier_x_list = [(0,0),(3,5)]

__cellSize__ = 20
__screenSize__ = tuple(map(lambda x: int(x*__cellSize__), grid_size))

def main():
    print(__screenSize__)
    scene = s.GameScene(__cellSize__,grid_size,player_pos,barrier_h,barrier_x_list)
    done = False
    clock = pygame.time.Clock()
    pause_time = 1
    start_time = time.time()
    while not done:
        clock.tick(20)
        done = scene.events()
        if not scene._pause and time.time() - start_time > pause_time:
            print("Update")
            start_time = time.time()
            done = scene.update()
        scene.drawMe()
        pygame.display.flip()
    pygame.quit()

main()
