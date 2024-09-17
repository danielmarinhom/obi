v, e = map(int,input().split())
grafo = [[] for _ in range(v)]
for _ in range(e):
  u, v = map(int,input().split())
  grafo[u].append(v)

def dfs(grafo, stack, vertex, visited):
  visited[vertex] = True
  for neighbor in grafo[vertex]:
    if not visited[neighbor]:
      dfs(grafo,stack,neighbor,visited)
  stack.append(vertex)
def transpose(grafo, n):
  transposed = [[] for _ in range(n)]
  for u,v in grafo:
    transposed[v].append(u)
  return transposed
def dfs2(grafo, vertex, component, visited):
  visited[vertex] = True
  component.append(vertex)
  for neighbor in grafo[vertex]:
    if not visited[neighbor]:
      dfs2(grafo,neighbor,component,visited)


