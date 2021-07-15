def insertion_sort(array):
    size = len(array)
    for i in range(1, size):
        j = i
        while j > 0 and array[j-1] > array[j]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
    return array

array = [3, 8, 9 ,5, 2, 1]
#if array is nearly sorted, insertion_sort is better than quick sort


print(insertion_sort(array))
