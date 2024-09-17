#N e E - vertices e arestas
#E linhas contem u,v,w
#S, vertice de origem

n,e = map(int,input().split())
grafo = []
for _ in range(e):
  u,v,w = map(int,input().split())
  grafo.append((u-1,v-1,w))
s = int(input())

def bellman_ford(arestas,num_vertices,start):
  start-=1
  distancia = [float('inf')] * num_vertices
  distancia[start] = 0
  for _ in range(num_vertices-1):
    for u,v,w in arestas:
      if distancia[u] != float('inf') and distancia[u] + w < distancia[v]:
        distancia[v] = distancia[u]+w
  for u,v,w in arestas:
      if distancia[u] != float('inf') and distancia[u] + w < distancia[v]:
        return "Ciclo negativo detectado"
  return [dist if dist != float('inf') else 'INF' for dist in distancia]

print(bellman_ford(grafo, n, s))