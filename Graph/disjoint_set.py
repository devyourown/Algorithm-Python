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

node, edges = map(int, input().split())
parent = [0] * (node+1)

for i in range(1, node+1):
    parent[i] = i

for i in range(edges):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합: ', end='')
for i in range(1, node+1):
    print(find_parent(parent, i), end=' ')

for i in range(1, node+1):
    print(parent[i])
