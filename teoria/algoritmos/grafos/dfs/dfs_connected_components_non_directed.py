def dfs(grafo, vertex, visited, component):
  visited[vertex] = True
  component.append(vertex)
  for neighbor in grafo[vertex]:
    if not visited[neighbor]:
      dfs(grafo,neighbor,visited,component)

def find_connected_components(grafo,n):
  visited = [False] * (n+1)
  components = []
  for node in range(1,n+1):
    if not visited[node]:
      component = []
      dfs(grafo,node,visited,component)
      components.append(component)
  return components

n = 6
grafo = [[] for _ in range(n+1)]
edges = [(1,2),(2,3),(2,4),(5,6)]
for u,v in edges:
  grafo[u].append(v)
  grafo[v].append(u)