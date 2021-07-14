def move_board(now, direct_alphabet):
    now_x, now_y = 0, 0
    for shape in range(len(direction)):
        if direction[shape] == direct_alphabet:
            now_x = now[0] + direction_x[shape]
            now_y = now[1] + direction_y[shape]
            if now_x < 1 or now_x > board_size or now_y < 1 or now_y > board_size:
                return False
            now[0], now[1] = now_x, now_y
            return True


if "__main__" == __name__:

    board_size = int(input())
    direction = ['L', 'R', 'U', 'D']
    direction_x = [0, 0, -1, 1]
    direction_y = [-1, 1, 0, 0]
    plan = list(input().split())
    now_xy = [1, 1]
    size = len(plan)
    for i in range(size):
        move_board(now_xy, plan[i])

    print(now_xy[0], now_xy[1])
