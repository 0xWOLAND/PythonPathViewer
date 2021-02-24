import math
from random import random
def generateMaze(draw, grid, maze, rows):
    maze[1][1] = 0
    on = [1, 1]

    while (not complete(maze)):

        n = neighbors(maze, on[0], on[1])
        if (len(n) == 0):
            t = findCoord(maze)
            on = t[0]

            maze[on[0]][on[1]] = 0
            maze[(on[0] + t[1][0]) // 2][(on[1] + t[1][1]) // 2] = 0

        else:

            i = math.floor(random() * len(n))
            nb = n[i]
            
            maze[nb[0]][nb[1]] = 0
            maze[(nb[0] + on[0]) // 2][(nb[1] + on[1]) // 2] = 0

            on = nb
        for row in range(rows):
            for col in range(rows):
                if(maze[row][col]):
                    grid[row][col].make_barrier()
                else:
                    grid[row][col].reset()
        draw()

   
    return grid


def neighbors(maze, ic, jc):
    final = []
    for i in range(0, 4):
        n = [ic, jc]

        n[i % 2] += ((math.floor(i / 2) * 2) or -2)
        if (n[0] < len(maze) and
            n[1] < len(maze[0]) and
            n[0] > 0 and
                n[1] > 0):

            if (maze[n[0]][n[1]] == 1):
                final.append(n)
    return final


def neighborsAB(maze, ic, jc):
    final = []
    for i in range(0, 4):
        n = [ic, jc]

        n[i % 2] += ((math.floor(i / 2) * 2) or -2)
        if (n[0] < len(maze) and
            n[1] < len(maze[0]) and
            n[0] > 0 and
                n[1] > 0):

            final.append(n)

    return final


def complete(maze):
    for i in range(1, len(maze), 2):
        for j in range(1, len(maze), 2):
            if (maze[i][j] != 0):
                return False
    return True


def findCoord(maze):
    for i in range(1, len(maze), 2):
        for j in range(1, len(maze), 2):

            if (maze[i][j] == 1):
                n = neighborsAB(maze, i, j)

                for k in range(0, len(n)):
                    if (maze[n[k][0]][n[k][1]] == 0):
                      return [[i, j], n[k]]
