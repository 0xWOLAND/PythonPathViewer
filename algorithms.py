from queue import PriorityQueue
import pygame


def backtrace(draw, parent, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    reverse_list = path[1:-1]
    for spot in reverse_list:
        spot.make_path()
        draw()


def dfs(draw, grid, start, end):
    parent = {}
    queue = []
    queue.append(start)
    while(queue):
        node = queue.pop()
        if not node.is_start() and not node.is_end():
            node.make_current()
        if node == end:
            backtrace(draw, parent, start, end)
            return
        for adjacent in reversed(node.neighbors):
            if node not in queue and not adjacent.is_closed():
                parent[adjacent] = node
                queue.append(adjacent)
                if not adjacent.is_end() and not adjacent.is_start() and not adjacent.is_closed():
                    adjacent.make_open()

        draw()
        if not node.is_start() and not node.is_end():
            node.make_closed()


def bfs(draw, grid, start, end):
    parent = {}
    queue = []
    queue.append(start)
    while(queue):
        node = queue.pop(0)
        if not node.is_start() and not node.is_end():
            node.make_current()
        if node == end:
            backtrace(draw, parent, start, end)
            return
        for adjacent in node.neighbors:
            if node not in queue and not adjacent.is_closed():
                parent[adjacent] = node
                queue.append(adjacent)
                if not adjacent.is_end() and not adjacent.is_start() and not adjacent.is_closed():
                    adjacent.make_open()
        draw()
        if not node.is_start() and not node.is_end():
            node.make_closed()


def A_Star(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = dist(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
        current = open_set.get()[2]
        if not current.is_start() and not current.is_end():
            current.make_current()
        open_set_hash.remove(current)
        if current == end:
           backtrace(draw, came_from, start, end)
           end.make_end()
           return True
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1
            if temp_g_score < g_score[neighbor]:
               came_from[neighbor] = current
               g_score[neighbor] = temp_g_score
               f_score[neighbor] = temp_g_score + dist(neighbor.get_pos(), end.get_pos())
               if neighbor not in open_set_hash:
                   count += 1
                   open_set.put((f_score[neighbor], count, neighbor))
                   open_set_hash.add(neighbor)
                   neighbor.make_open()
        draw()
        if current != start:
           current.make_closed()
    return False

def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
