width = int(input())

possible_filling = [0] * 1001

possible_filling[1] = 1
possible_filling[2] = 3

for i in range(3, width+1):
    possible_filling[i] = (possible_filling[i-1] + 2 * possible_filling[i-2])


print(possible_filling[width] % 796796)
