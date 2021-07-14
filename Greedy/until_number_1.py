number, dividing_num = map(int, input().split())

count = 0
while 1 != number:
    if 0 == (number%dividing_num):
        number /= dividing_num
        count += 1
    else :
        number -= 1
        count += 1
print(count)
