import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

citys, paths, c = map(int, input().split())
graph = [[] for _ in range(citys+1)]
distance = [INF] * (citys+1)

for _ in range(paths):
    x, toY, weight = map(int, input().split())
    graph[x].append((toY, weight))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        cost, now = heapq.heappop(q)
        if distance[now] < cost:
            continue

        distance[now] = cost

        for dest, time in graph[now]:
            if distance[dest] > cost + time:
                distance[dest] = cost + time
                heapq.heappush(q, (cost+time, dest))

dijkstra(c)

count_city = 0
max_time = 0
for i in range(2, citys+1):
    if distance[i] == INF:
        continue
    else:
        count_city += 1
        if max_time < distance[i]:
            max_time = distance[i]
print(count_city, max_time)
