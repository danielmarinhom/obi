n = int(input())
m = int(input())
grafo = []
for _ in range(m):
    u, v, t = map(int, input().split())
    grafo.append((u-1, v-1, t)) #lista de tuplas
  
def floyd_warshall(grafo, n):
  dist = [[float('inf')] * n for _ in range(n)]
  for i in range(n):    #distancia do vertice para ele mesmo = 0
    dist[i][i] = 0
    
  for u, v, t in grafo:
    dist[u][v] = t

  for k in range(n):
    for i in range(n):
      for j in range(n):
        if dist[i][j] > dist[i][k] + dist[k][j]:
          dist[i][j] = dist[i][k] + dist[k][j]
  return dist