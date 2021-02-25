import pygame
from pygame.locals import *
import math
from algorithms import bfs, dfs, A_Star
from maze import generateMaze
from random import randint


WIDTH = 900
HEIGHT = 900
FPS = 240
clock = pygame.time.Clock()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Path Finding Algorithm Visualizer")

# Colors

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255,165,0)
PURPLE = (128, 0, 128)
TURQUOISE = (64,224,208)
GREY = (192,192,192)
class Spot: 
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED
    
    def is_open(self):
        return self.color == GREEN
    
    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE
    
    def is_end(self):
        return self.color == TURQUOISE
    
    def is_current(self):
        return self.color == BLUE

    def reset(self):
        self.color = WHITE

    def make_closed(self):
        self.color = RED
    
    def make_open(self):
        self.color = GREEN
    
    def make_barrier(self):
        self.color = BLACK

    def make_start(self):
        self.color = ORANGE
    
    def make_end(self):
        self.color = TURQUOISE
    
    def make_path(self):
        self.color = PURPLE
    
    def make_current(self):
        self.color = BLUE
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])
        

    def __lt__(self, other):
        return False





def make_grid(rows, width, generate_grid=False):
    grid = []
    visited = []
    gap = math.ceil(width / rows)
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)
    for i in range(rows ):
        visited.append([])
        for j in range(rows):
            grid[i][j].reset()
            visited[i].append(1)
    if generate_grid:
        grid = generateMaze((lambda: draw(WIN, grid, rows, width)), grid, visited, rows)
   
    return grid

def draw_grid(win, rows, width):
    gap = math.ceil(width / rows)
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
    for j in range(rows):
        pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)
    
    draw_grid(win, rows, width)
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap
    print("({}, {})".format(row, col))
    return min(row, rows - 1), min(col, rows - 1)



def main(win, width):
    ROWS = 75
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    started = False

    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False
            
            if started:
                continue

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start and spot != end:
                    start = spot
                    spot.make_start()
                elif not end and spot != start:
                    end = spot
                    spot.make_end()
                elif spot != end and spot != start:
                    spot.make_barrier()
                
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                if spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d and not started:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)

                    dfs(lambda: draw(win, grid, ROWS, width), grid, start, end)
                elif event.key == pygame.K_b and not started:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)

                    bfs(lambda: draw(win, grid, ROWS, width), grid, start, end)
                elif event.key == pygame.K_a and not started:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)

                    A_Star(lambda: draw(win, grid, ROWS, width), grid, start, end)
                
                elif event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)
                elif event.key == pygame.K_m:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width, True)
        clock.tick(FPS)
        
                

    pygame.quit()

main(WIN, WIDTH)