x = int(input())
count_list = [0] * 30001
for i in range(2, x+1):
    count_list[i] = count_list[i-1] + 1
    if i%2 == 0:
        count_list[i] = min(count_list[i], count_list[i//2] + 1)
    if i%3 == 0:
        count_list[i] = min(count_list[i], count_list[i//3] + 1)
    if i%5 == 0:
        count_list[i] = min(count_list[i], count_list[i//5] + 1)


print(count_list[x])
