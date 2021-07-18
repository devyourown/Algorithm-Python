types, money = map(int, input().split())

type_list = list()

money_list = [10001] * (money+1)

for i in range(types):
    type_list.append(int(input()))
    money_list[type_list[i]] = 1

money_list[0] = 0

for i in range(1, money+1):
    for types in type_list:
        if i % types == 0:
            money_list[i] = min(money_list[i-types]+1, i/types)

if money_list[money] == 10001:
    print(-1)
else:
    print(money_list[money])
