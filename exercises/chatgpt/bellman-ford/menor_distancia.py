n,m = map(int,input().split()) #vertices, arestas
conexoes = []
for _ in range(m):
  u,v,w = map(int,input().split())
  conexoes.append((u,v,w))

def bellman(edges,num_vertices,inicio):
  dist = [float('inf')] * num_vertices
  dist[inicio] = 0
  for _ in range(num_vertices-1):
    for u,v,w in edges:
      if dist[u] != float('inf') and dist[u]+w < dist[v]:
        dist[v] = dist[u] + w
  for u,v,w in edges:
    if dist[u] != float('inf') and dist[u] + w < dist[v]:
      dist[v] = dist[u] + w
  return dist

print(bellman(conexoes,n,1))