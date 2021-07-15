def dfs(graph, node, visited):
    visited[node] = True
    print(node, end=" ")

    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(graph, next_node, visited)



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

visited = [False] * (1+len(graph))

dfs(graph, 1, visited)
