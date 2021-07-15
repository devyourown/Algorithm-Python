ice_board_y, ice_board_x = map(int, input().split())
ice_board = [[0 for _ in range(ice_board_x)] for _ in range(ice_board_y+1)]
ice_board[0] = list()

for y in range(1, ice_board_y+1):
    ice_board[y] = list(map(int, input().split()))

def dfs(graph, y, x):
    graph[y][x] = 1
    if x+1 < ice_board_x and graph[y][x+1] == 0:
        dfs(graph, y, x+1)
    if y+1 < ice_board_y and graph[y+1][x] == 0:
        dfs(graph, y+1, x)
    if x-1 < ice_board_x and graph[y][x-1] == 0:
        dfs(graph, y, x-1)

count = 0

for y in range(1, ice_board_y+1):
    for x in range(ice_board_x):
        if ice_board[y][x] == 0:
            dfs(ice_board, y, x)
            count += 1

print(count)
