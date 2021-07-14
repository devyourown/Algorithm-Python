map_y_size, map_x_size = map(int, input().split())

def rotate(direct):
    if direct == 0:
        return 3
    else:
        return direct-1

def isOutOfIndex(possible_y, possible_x):
    if 0 <= possible_y < map_y_size and 0 <= possible_x < map_x_size:
        return False
    else :
        return True

def isVisited(possible_y, possible_x):
    for visit_y, visit_x in visited:
        if visit_y == possible_y and visit_x == possible_x:
            return True
    return False

def isOcean(possible_y, possible_x):
    if game_map[possible_y][possible_x] == 1 :
        return True
    return False

move_y = [-1, 0, 1, 0]
move_x = [0, 1, 0, -1]

character_y, character_x, character_direction = map(int, input().split())
#game_map = [[0 for i in range(map_y_size)] for j in range(map_x_size)]
game_map = [[0 for col in range(map_y_size)] for row in range(map_x_size)]
direction = ['North', 'East', 'South', 'Western']
visited = list()
visited.append([character_y, character_x])

for i in range(map_y_size):
    game_map[i] = list(map(int, input().split()))

exit_count = 0

while True:
    if exit_count == 3:
        back_y, back_x = character_y+move_y[character_direction-2], character_x+move_x[character_direction-2]
        if isOcean(back_y, back_x):
            break
        else:
            character_y = back_y
            character_x = back_x
    possible_direction = rotate(character_direction)
    possible_y = character_y + move_y[possible_direction]
    possible_x = character_x + move_x[possible_direction]
    if not isOutOfIndex(possible_y, possible_x) and not isVisited(possible_y, possible_x) and not isOcean(possible_y, possible_x):
        visited.append([possible_y, possible_x])
        character_y = possible_y
        character_x = possible_x
        character_direction = possible_direction
        exit_count = 0
    else:
        exit_count += 1
        character_direction = possible_direction

print(len(visited))
