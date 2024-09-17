n = int(input())
grafo = []
for _ in range(n):
  u,v,w = map(int,input().split())
  grafo.append((u,v,w))

def floyd_warshall(grafo,n):
  dist = [[float('inf')]*n for _ in range(n)]
  for i in range(n):
    dist[i][i] = 0
  for u,v,t in grafo:
    dist[u][v] = t

  for k in range(n):
    for i in range(n):
      for j in range(n):
        if dist[i][j] > dist[i][k] + dist[k][j]:
          dist[i][j] = dist[i][k] + dist[k][j]
  return dist

res = floyd_warshall(grafo,n)
for linha in res:
  print(linha)