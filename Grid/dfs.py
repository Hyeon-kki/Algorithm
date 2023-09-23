def dfs(graph, visitied, node_idx):
    visitied[node_idx] = True
    print(node_idx, end=" ")
    for node in graph[node_idx]:
        if not visitied[node]:
            dfs(graph, visitied, node)
            
graph = [
    [],
    [2,3,8],
    [1,7],
    [4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9

dfs(graph, visited, 1)