#directed
n,m = map(int,input().split()) # vertex, edge
edges = []
for _ in range(m):
  u,v = map(int,input().split())
  edges.append((u,v))
grafo = [[] for _ in range(n+1)]
for u,v in edges:
  grafo[u].append(v)

def dfs1(grafo, stack, visited, node):
  visited[node] = True
  for neighbor in grafo[node]:
    if not visited[neighbor]:
      dfs1(grafo, stack, visited, neighbor)
  stack.append(node)

def transpose_graph(grafo,n):
  transposed = [[] for _ in range(n+1)]
  for u in range(n+1):
    for v in grafo[u]:
      transposed[v].append(u)
  return transposed

def dfs2(grafo, visited, node, elements):
  visited[node] = True
  elements.append(node)
  for neighbor in grafo[node]:
    if not visited[neighbor]:
      dfs2(grafo, visited, neighbor, elements)

def sccs(grafo, n):
  visited = [False] * (n+1)
  stack = []
  for node in range(1, n+1):
    if not visited[node]:
      dfs1(grafo,  stack, visited, node)
  transposed = transpose_graph(grafo,n)
  visited = [False] * (n+1)
  sccs = []
  while stack:
    node = stack.pop()
    if not visited[node]:
      elements = []
      dfs2(transposed, visited, node, elements)
      sccs.append(elements)
  return sccs
sccs = sccs(grafo, n)
print(len(sccs), len(sccs)-1)