quantity_of_warehouse = int(input())
warehouses = list(map(int, input().split()))

sum_of_warehouse = [0] * 101

sum_of_warehouse[0] = warehouses[0]
sum_of_warehouse[1] = warehouses[1]
sum_of_warehouse[2] = warehouses[0] + warehouses[2]

for i in range(3, quantity_of_warehouse):
    if sum_of_warehouse[i-2] > sum_of_warehouse[i-3]:
        sum_of_warehouse[i] = sum_of_warehouse[i-2] + warehouses[i]
    else :
        sum_of_warehouse[i] = sum_of_warehouse[i-3] + warehouses[i]

print(sum_of_warehouse[quantity_of_warehouse-1])
