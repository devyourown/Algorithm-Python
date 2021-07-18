import sys
input = sys.stdin.readline
INF = int(1e9)

num_of_nodes, links = map(int, input().split())
start = int(input())
graph = [[] for i in range(num_of_nodes+1)]
visited = [False]  * (num_of_nodes+1)
distance = [INF] * (num_of_nodes+1)

for _ in range(links):
    node, toNode, weight = map(int, input().split())
    graph[node].append((toNode, weight))


def get_smallest_node_index():
    min_distance = INF
    min_index = 0
    for i in range(1, num_of_nodes+1):
        if min_distance > distance[i] and not visited[i]:
            min_index = i
            min_distance = distance[i]
    return min_index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for dest, weight in graph[start]:
        distance[dest] = weight

    for i in range(num_of_nodes-1):
        small_node_index = get_smallest_node_index()
        visited[small_node_index] = True
        for dest, weight in graph[small_node_index]:
            if distance[dest] > distance[small_node_index] + weight:
                distance[dest] = distance[small_node_index] + weight

dijkstra(start)

for i in range(1, num_of_nodes+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])
