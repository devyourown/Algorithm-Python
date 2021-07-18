all_parts = int(input())
list_num_of_parts = list(map(int, input().split()))
requested_parts = int(input())
list_requested_parts = list(map(int, input().split()))

list_num_of_parts.sort()

def binary_search(array, left, right, object):
    if left > right:
        return None
    mid = (left+right) // 2

    if object == array[mid]:
        return mid
    elif object > array[mid]:
        return binary_search(array, mid+1, right, object)
    else :
        return binary_search(array, left, mid-1, object)

for i in range(requested_parts):
    if binary_search(list_num_of_parts, 0, all_parts-1, list_requested_parts[i]) is None :
        print('no', end=' ')
    else :
        print('yes', end=' ')
