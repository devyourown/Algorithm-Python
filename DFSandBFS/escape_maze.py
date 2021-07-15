maze_y, maze_x = map(int, input().split())

maze = []
for y in range(maze_y):
    maze.append(list(map(int, input().split())))

INF = 987654321

def escape(maze, y, x):
    if y == maze_y-1 and x == maze_x-1:
        return 1

    if 0 > y or y >= maze_y or 0 > x or x >= maze_x:
        return INF

    if maze[y][x] == 0:
        return INF

    maze[y][x] = 0
    east = 1 + escape(maze, y, x+1)
    west = 1 + escape(maze, y, x-1)
    south = 1 + escape(maze, y-1, x)
    north = 1 + escape(maze, y+1, x)
    return min([east, west, south, north])

print(escape(maze, 0, 0))
