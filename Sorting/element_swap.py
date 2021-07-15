num_of_elements, num_of_swap = map(int, input().split())

list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

list_a.sort()
list_b.sort(reverse=True)
for i in range(num_of_swap):
    if list_a[i] < list_b[i]:
        list_a[i], list_b[i] = list_b[i], list_a[i]
    else :
        break

result = 0
for i in range(len(list_a)):
    result += list_a[i]
print(result)
