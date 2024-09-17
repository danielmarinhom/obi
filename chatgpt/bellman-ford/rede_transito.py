n,m = map(int,input().split())
edges = []
for _ in range(m):
  u,v,w = map(int,input().split())
  edges.append((u-1,v-1,w))
s = int(input())
s -=1


def bellman_ford(edges, n, s):
  dist = [float('inf')]*n
  dist[s] = 0
  for _ in range(n-1):
    for u,v,w in edges:
      if dist[u] != float('inf') and dist[u]+w < dist[v]:
        dist[v] = dist[u]+w
  for u,v,w in edges:
    if dist[u] != float('inf') and dist[u]+w < dist[v]:
      return None
  return dist
res = bellman_ford(edges,n,s)

if res:
  for d in res:
    if d != float('inf'):
      print(d)
else:
  print("Ciclo Negativo Detectado")
      