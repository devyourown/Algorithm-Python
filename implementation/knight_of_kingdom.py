position = input()

knight_possible_dy = [2, 1, -1, -2, -2, -1, 1, 2]
knight_possible_dx = [1, 2, 2, 1, -1, -2, -2, -1]

present_loc_x = 0
present_loc_y = int(position[1])
count = 0

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for alpha in range(len(alphabet)):
    if position[0] == alphabet[alpha]:
        present_loc_x = alpha

for i in range(8):
    possible_x = present_loc_x + knight_possible_dx[i]
    possible_y = present_loc_y + knight_possible_dy[i]
    if 1 <= possible_x <= 8 and 1 <= possible_y <= 8:
        count += 1

print(count)
