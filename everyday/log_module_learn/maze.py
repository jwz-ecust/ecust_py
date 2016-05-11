# -*- coding: utf-8 -*-
import random

def initMaze():
    maze = [[0] * 22 for _ in range(22)]
    walls = [
        (1, 3),
        (2, 1),
        (2, 5),
        (3, 3),
        (3, 4),
        (4, 2),
        (5,4)
    ]
    for i in range(22):
        maze[i][0] = maze[i][-1] = 1
        maze[0][i] = maze[-1][i] = 1
    for i, j in walls:
        maze[i][j] = 1
    return maze

# maze = initMaze()
'''
1   1 1 1 1 1   1


1   0 0 1 0 0   1

1   1 0 0 0 1   1

1   0 0 1 1 0   1

1   0 1 0 0 0   1

1   0 0 0 1 0   1


1   1 1 1 1 1   1
'''


def path(maze, start, end):
    i, j = start
    ei, ej = end
    stack = [(i, j)]
    maze[i][j] = 1
    while stack:
        i, j = stack[-1]
        if (i, j) == (ei, ej):
            break
        while True:
            select = [(0, -1), (0, 1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
            di, dj = random.choice(select)
            # print di, dj
            # print maze[i + di][j + dj]
        # for di, dj in [(1, 1), (-1, -1), (1, -1), (-1, 1) ,(0, -1), (0, 1), (1, 0), (-1, 0)]:
            if maze[i + di][j + dj] == 0:
                maze[i + di][j + dj] = 1
                stack.append((i + di, j + dj))
                break
        else:
            stack.pop()
    return stack


Maze = initMaze()
result = path(Maze, start=(1, 1), end=(20, 20))

print result
