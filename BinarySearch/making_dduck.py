num_of_dduck, requested_length = map(int, input().split())
list_of_dduck = list(map(int, input().split()))

max_length = 0

def is_optimal_length(array, height, length):
    for dduck in array:
        if dduck > height:
            length -= dduck - height
    return length


for dduck in list_of_dduck:
    if max_length < dduck:
        max_length = dduck

left = 0
right = max_length-1
result = 0

while left <= right:
    mid = (left+right)//2

    left_length = is_optimal_length(list_of_dduck, mid, requested_length)
    if left_length > 0:
        right = mid-1
    else :
        result = mid
        left = mid+1
print(result)
