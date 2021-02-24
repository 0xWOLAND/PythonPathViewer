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
        print("({}, {})".format(node.get_pos()[0], node.get_pos()[1]))
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
        
