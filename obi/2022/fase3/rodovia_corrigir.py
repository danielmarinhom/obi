def dfs(grafo, stack, vertex, visited):
  visited[vertex] = True
  for neighbor in grafo[vertex]:
    if not visited[neighbor]:
      dfs(grafo,stack,neighbor,visited)
  stack.append(vertex)

def transpose(grafo, n):
  #(x, y) , (y, x)
  transposed = [[] for _ in range(n)]
  for x in range(n):
    for y in grafo[x]:
      transposed[y].append(x)
  return transposed

def dfs2(grafo, component, vertex, visited):
  visited[vertex] = True
  component.append(vertex)
  for neighbor in grafo[vertex]:
    if not visited[neighbor]:
      dfs2(grafo,component,neighbor,visited)

def find_sccs(grafo,n):
  stack = []
  visited = [False]*(n+1)
  for node in range(1,n+1):
    if not visited[node]:
      dfs(grafo,stack,node,visited)

  transposed = transpose(grafo,n)
  visited = [False]*(n+1)
  sccs = []
  while stack:
    node = stack.pop(0)
    if not visited[node]:
      component = []
      dfs2(transposed,component,node,visited)
      sccs.append(component)
  return sccs






n,m = map(int,input().split())
grafo = [[] for _ in range(n)]
for _ in range(m):
  x,y = map(int,input().split())
  x-=1
  y-=1
  grafo[x].append(y)


