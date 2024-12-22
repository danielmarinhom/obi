def dfs(graph, vertex, visited, stack):
    visited[vertex] = True
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, stack)
    stack.append(vertex)

def transpose_graph(graph, n):
    transposed_graph = [[] for _ in range(n + 1)]
    for u in range(1, n + 1):
        for v in graph[u]:
            transposed_graph[v].append(u)
    return transposed_graph

def dfs_collect(graph, vertex, visited, component):
    visited[vertex] = True
    component.append(vertex)
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs_collect(graph, neighbor, visited, component)

def find_sccs(graph, n):
    # Step 1: Perform DFS to get the order of finish times
    visited = [False] * (n + 1)
    stack = [] #ordem de finalizacao
    for node in range(1, n + 1):
        if not visited[node]:
            dfs(graph, node, visited, stack) #adiciona o vertice a pilha

    # Step 2: Transpose the graph
    transposed_graph = transpose_graph(graph, n)

    # Step 3: Perform DFS on the transposed graph in the order of finish times
    visited = [False] * (n + 1)
    sccs = []
    while stack:
        node = stack.pop()
        if not visited[node]:
            component = []
            dfs_collect(transposed_graph, node, visited, component)
            sccs.append(component)

    return sccs

# Example usage:
n = 6
graph = [[] for _ in range(n + 1)]
edges = [(1, 2), (2, 3), (3, 1), (4, 5), (5, 6), (6, 4)]
for u, v in edges:
    graph[u].append(v)

sccs = find_sccs(graph, n)
print(f"Number of SCCs: {len(sccs)}")
for scc in sccs:
    print("SCC:", scc)
