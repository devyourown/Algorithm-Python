import sys
input = sys.stdin.readline
INF = int(1e9)


quantity_company, links = map(int, input().split())
graph = [[INF] * (quantity_company+1) for _ in range(quantity_company+1)]

for i in range(1, quantity_company+1):
    graph[i][i] = 0

for _ in range(1, links+1):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

dest, detour = map(int, input().split())

for k in range(1, quantity_company+1):
    for a in range(1, quantity_company+1):
        for b in range(1, quantity_company+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

if graph[1][detour] + graph[detour][dest] >= INF:
    print(-1)
else :
    print(graph[1][detour] + graph[detour][dest])
