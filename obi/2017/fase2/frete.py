n,m = map(int,input().split()) #vertices, arestas
edges = []
for _ in range(m):
  a,b,c = map(int,input().split())
  edges.append((a-1,b-1,c))

def bellman_ford(edges, n):
  dist = [float('inf')]*n
  dist[0] = 0
  for _ in range(n-1):
    for u,v,w in edges:
      if dist[u] != float('inf') and dist[u]+w < dist[v]:
        dist[v] = dist[u]+w
  return dist[n-1]
print(bellman_ford(edges, n))

#6 min