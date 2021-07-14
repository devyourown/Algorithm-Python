

list_quantity, add_quantity, add_limit = map(int, input().split())
numbers = list(map(int, input().split()))
result = 0

numbers.sort(reverse=True)
count = 0

second_number_add_quantity = add_quantity // (add_limit+1)
first_number_add_quantity = add_quantity - second_number_add_quantity

result = first_number_add_quantity * numbers[0] + second_number_add_quantity * numbers[1]

print(result)

#for i in range(add_quantity):
#    if(count == add_limit):
#        count = 0
#        result += numbers[1]
#        continue
#    result += numbers[0]
#    count += 1
#print(result)
