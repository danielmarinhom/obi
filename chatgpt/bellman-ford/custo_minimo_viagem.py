n,m,q = map(int,input().split()) #vertices, arestas, consultas
edges = []
for _ in range(m):
  u,v,w = map(int,input().split())
  edges.append((u-1,v-1,w))
consultas = []
for _ in range(q):
  origem, destino = map(int,input().split())
  consultas.append((origem-1,destino-1))


def bellman(s,edges, num_vertices):
  dist = [float('inf')]*num_vertices
  dist[s] = 0
  for _ in range(num_vertices-1):
    for u,v,w in edges:
      if dist[u] != float('inf') and dist[u]+w < dist[v]:
        dist[v] = dist[u]+w
  for u,v,w in edges:
    if dist[u] != float('inf') and dist[u]+w < dist[v]:
      return None
  return dist

for origem, destino in consultas:
  dist = bellman(origem,edges,n)
  if dist is None:
    print("Ciclo Negativo Detectado")
  elif dist[destino] == float('inf'):
    print("Inalcancavel")
  else:
    print(dist[destino])