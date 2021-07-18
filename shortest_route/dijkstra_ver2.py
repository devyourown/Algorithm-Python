import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

quantity_node, links = map(int, input().split())
start_index = int(input())
graph = [[] for _ in range(quantity_node+1)]
distance = [INF] * (quantity_node+1)

for _ in range(links):
    node, dest_node, weight = map(int, input().split())
    graph[node].append((dest_node, weight))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:

        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for dest, weight in graph[now]:
            if distance[dest] > dist+weight:
                distance[dest] = dist+weight
                heapq.heappush(q, (dist+weight, dest))

dijkstra(start_index)

for i in range(1, quantity_node+1):
    if distance[i] == INF:
        print('INFINITY')
    else :
        print(distance[i])
