hour = int(input())

count = 0

def check_3(time):
    if (time//10) == 3 or (time%10) == 3:
        return True
    else:
        return False

for ticking_hour in range(hour+1):
    if check_3(ticking_hour):
        count += 3600
        continue

    for ticking_minute in range(60):
        if check_3(ticking_minute):
            count += 60
            continue
        for ticking_second in range(60):
            if check_3(ticking_second):
                count += 1
                continue

print(count)

count = 0
for i in range(hour+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
