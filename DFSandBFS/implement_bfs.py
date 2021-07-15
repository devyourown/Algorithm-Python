from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for present_node in graph[node]:
            if not visited[present_node]:
                queue.append(present_node)
                visited[present_node] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7, 8],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * (len(graph)+1)

bfs(graph, 1, visited)
