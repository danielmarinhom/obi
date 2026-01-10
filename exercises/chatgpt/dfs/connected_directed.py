def dfs(grafo, vertex, visited, stack):
  visited[vertex] = True
  for neighbor in grafo[vertex]:
    if not visited[neighbor]:
      dfs(grafo, neighbor, visited, stack)
  stack.append(vertex)

def transpose(grafo,n):
  transposed = [[] for _ in range(n+1)]
  for u in range(1,n+1):
    for v in grafo[u]:
      transposed[v].append(u)
  return transposed

def dfs2(grafo, vertex, visited, element):
  visited[vertex] = True
  element.append(vertex)
  for neighbor in grafo[vertex]:
    if not visited[neighbor]:
      dfs2(grafo, neighbor, visited, element)

def sccs(grafo,n):
  stack = []
  visited = [False]*(n+1)
  for node in range(1,n+1):
    if not visited[node]:
      dfs(grafo,node,visited,stack)
  
  transposed = transpose(grafo,n)

  sccs = []
  visited = [False]*(n+1)
  while stack:
    node = stack.pop()
    if not visited[node]:
      element = []
      dfs(transposed,node,visited,element)
      sccs.append(element)
  return sccs

n,m = map(int,input().split())
grafo = [[] for _ in range(n+1)]
for _ in range(m):
  u,v = map(int,input().split())
  grafo[u].append(v)

print(sccs(grafo,n))