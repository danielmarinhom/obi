n,m = map(int,input().split())
edges = []
for _ in range(m):
  u,v,w = map(int,input().split())
  edges.append((u-1,v-1,w))
def bellman(edges, n):
  dist = [float('inf')] * n
  dist[0] = 0
  for _ in range(n-1):
    for u,v,w in edges:
      if dist[u] != float('inf') and dist[u]+w < dist[v]:
        dist[v] = dist[u]+w
  for u,v,w in edges:
    if dist[u] != float('inf') and dist[u]+w < dist[v]:
      return "Ciclo Negativo Encontrado"
  return "Sem Ciclo Negativo"
print(bellman(edges, n))