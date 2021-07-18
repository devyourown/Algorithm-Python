def fibo(number):
    if number == 1 or number == 2:
        d[number] = 1
        return d[number]
    if d[number] != 0:
        return d[number]

    d[number] = fibo(number-1) + fibo(number-2)
    return d[number]

d = [0] * 1001

print(fibo(100))
