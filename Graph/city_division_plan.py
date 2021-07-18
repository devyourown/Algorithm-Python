def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b

num_of_house, num_of_road = map(int, input().split())
parent = [0] * (num_of_house+1)

for i in range(1, num_of_house+1):
    parent[i] = i

edges = []

for _ in range(num_of_road):
    a, b, weight = map(int, input().split())
    edges.append((weight, a, b))

edges.sort()
result = list()
final_sum = 0

for edge in edges:
    weight, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result.append(weight)

for i in range(len(result)-1):
    final_sum += result[i]
print(final_sum)
