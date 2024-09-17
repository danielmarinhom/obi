#grafo direcionado
#cada vertice representa um cruzamento e cada aresta uma rua

n = int(input())
m = int(input())
grafo = []
for _ in range(m):
  u,v,t = map(int,input().split())
  grafo.append((u-1,v-1,t))

nbloqueadas = int(input())
bloqueadas = []
for _ in range(nbloqueadas):
  u,v = map(int,input().split())
  bloqueadas.append((u-1,v-1))

def floyd_warshall(grafo,n, bloqueadas):
  dist = [[float('inf')]*n for _ in range(n)]
  for i in range(n):
    dist[i][i] = 0
  novografo = [edge for edge in grafo if (edge[0], edge[1]) not in bloqueadas]
  for u,v,t in novografo:
    if (u,v) not in bloqueadas:
      dist[u][v] = t
  
  for k in range(n):
    for i in range(n):
      for j in range(n):
        if dist[i][j] > dist[i][k] + dist[k][j]:
          dist[i][j] = dist[i][k] + dist[k][j]

  for i in range(n):
    for j in range(n):
      if dist[i][j] == float('inf'):
        dist[i][j] = "INF"
  
  return dist

res = floyd_warshall(grafo, n, bloqueadas)
for linha in res:
  print(" ".join(map(str,linha)))