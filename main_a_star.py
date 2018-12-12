import a_star as a
import numpy as np
import math
import json

node_list = []

def create_walls(wall_list,node_list):
    for wall in wall_list:
        n = a.node((wall[0],wall[1],a.nodeState.WALL,1))
        node_list.append(n)
        update_grid(n)

def update_grid(n):
    grid[n.state[0],n.state[1]] = n.state[2].value

size = (5,5)
grid = np.zeros(size)
print(grid)

start = a.node((0,0,a.nodeState.START))
start.boundary = True
final = a.node((4,4,a.nodeState.FINAL))
final.f = math.inf

node_list.append(start)
update_grid(start)
node_list.append(final)
update_grid(final)
wall_list=[(1,0),(1,2),(1,1),(1,3),(3,4),(4,2),(4,1),(3,2),(2,2)]
create_walls(wall_list,node_list)
path = a.astar(node_list,start,final,size)
if path:
    while(path):
        print(path.state)
        if not a.equals(path,start) and not a.equals(path,final):
            path.state = (path.state[0],path.state[1],a.nodeState.PATH)
            update_grid(path)
        path = path.father
    print(grid)
else:
    print('No path found')
