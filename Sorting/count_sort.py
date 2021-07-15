def count_sort(array):
    count_array = [0] * (max(array)+1)

    for i in range(len(array)):
        count_array[array[i]] += 1

    return count_array

array = [3, 4, 9, 0, 4, 2, 3, 5, 1, 5, 2,7, 5, 6, 9, 0, 2]
result = count_sort(array)

for i in range(len(result)):
    for j in range(result[i]):
        print(i, end=" ")
