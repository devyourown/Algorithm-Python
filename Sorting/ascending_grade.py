number_of_students = int(input())

grade_list = list()

for i in range(number_of_students):
    name, grade = input().split()
    grade_list.append([name, int(grade)])

def second_data_sort(data):
    return data[1]
sorted_list = sorted(grade_list, key=second_data_sort)
for name, grade in sorted_list:
    print(name, end=" ")
