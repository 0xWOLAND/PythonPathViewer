![image](https://storage.googleapis.com/replit/images/1614213768648_3a7047c1d374416565182a55edf93aac.png)
# Getting Started
A pathfinder using Pygame to visualize the A* Algorithm, Depth-First Search, and Breadth-First Search.

### Controls
- c: Clear Board
- m: Generate Maze (Hunt and Kill Algorithm)
- b: Breadth-First Search
- d: Depth-First Search
- a: A* Algorithm

### Run Code
If you want to run this file locally, clone my Github repository [here](https://github.com/bhargavannem/PythonPathViewer). Then, run the following:
```
python main.py
```


# Algorithms
### Depth-first search (DFS)
Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.

![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Depth-First-Search.gif/220px-Depth-First-Search.gif)
##### Complexity
- Worst complexity: O(|V| + |E|) 
- Space complexity: O(|V|)

### Breadth-first search (BFS)
Breadth-first search is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root, and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.

![alt text](https://upload.wikimedia.org/wikipedia/commons/4/46/Animated_BFS.gif)
##### Complexity
- Worst complexity: O(|E|) 
- Space complexity: O(|V|)

### A* search algorithm
A* is a graph traversal and path search algorithm, which is often used in many fields of computer science due to its completeness, optimality, and optimal efficiency. One major practical drawback is its O(b^d) space complexity, as it stores all generated nodes in memory.

![alt text](https://upload.wikimedia.org/wikipedia/commons/5/5d/Astar_progress_animation.gif)
##### Complexity
- Worst complexity: O(|E|) 
- Space complexity: O(|V|)

### Hunt and Kill Maze Generation Algorithm
The hunt-and-kill algorithm is in many ways the same as the backtracking algorithm in that it creates long winding paths. However, where the backtracking algorithm backtracks, the hunt-and-kill algorithm simply searches iteratively. This means that when it curls itself into a corner, it gives up on that and looks for the "first" (left to right, one row at a time) cell that neighbors part of the maze. It then continues building the maze from there. 

# About Me
Hi! My name is Bhargav and I am a developer in Austin, Texas. You can check out some of my other projects [here](https://github.com/bhargavannem/). 