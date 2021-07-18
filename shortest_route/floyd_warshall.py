INF = int(1e9)
num_of_nodes = int(input())
links = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    graph[a][a] = 0

for _ in range(links):
    a, to_b, weight = map(int, input().split())
    graph[a][to_b] = weight

#floyd-warshall
for detour in (1, num_of_nodes+1):
    for node_a in (1, num_of_nodes+1):
        for node_b in (1, num_of_nodes+1):
            graph[node_a][node_b] =
            min(graph[node_a][node_b], graph[node_a][detour] + graph[detour][node_b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] = INF:
            print("INFINTY", end=" ")
        else :
            print(graph[a][b], end=" ")
    print()
