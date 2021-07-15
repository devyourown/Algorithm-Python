quantity = int(input())

array = list()

for i in range(quantity):
    array.append(int(input()))

array.sort(reverse=True)
print(array)
