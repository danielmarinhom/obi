
n, b = map(int,input().split()) #numero de ilhas, numero de barcos (vertices, arestas)
conexoes = []
parent = [i for i in range(n)]
for _ in range(b):
  i, j, p = map(int,input().split())
  conexoes.append((i,j,p))

def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]
def union(a,b):
  rootA = find(a)
  rootB = find(b)
  if rootA != rootB:
    if rootA > rootB:
      parent[rootB] = rootA
    else:
      parent[rootA] = rootB
def kruskal(edges, num_vertices):
  edges.sort(key=lambda x: x[2])
  mst, mst_weight = [], 0
  for u,v,w in edges:
    if find(u) != find(v):
      union(u,v)
      mst.append((u,v,w))
      mst_weight+=w
      if len(mst) == num_vertices-1:
        break
  return mst

def bfs(mst, start, end, n):
  adj = [[] for _ in range(n)]
  for u,v,w in mst:
    adj[u].append((v,w))
    adj[v].append((u,w))
  max_passengers = [0]*n
  max_passengers[start] = float('inf')
  queue = [start]
  visited = [False]*n
  visited[start] = True
  while queue:
    node = queue.pop(0)
    for neighbor, weight in adj[node]:
      if not visited[neighbor]:
        visited[neighbor] = True
        max_passengers[neighbor] = min(max_passengers[node],weight)
        queue.append(neighbor)
        if neighbor == end:
          return max_passengers[neighbor]
  return 0


