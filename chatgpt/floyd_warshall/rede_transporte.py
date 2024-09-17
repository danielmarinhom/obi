n = int(input)
m = int(input)
matriz = [[-1] * n for _ in range(n)]
for _ in range(m):
  u,v,t = map(int,input().split())
  matriz[u-1][v-1] = t

def floyd(matriz, n):
  dist = [[float('inf')]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if i == j:
        dist[i][j] = 0
      elif matriz[i][j] == -1:
        dist[i][j] = matriz[i][j]
  
  for k in range(n):
    for i in range(n):
      for j in range(n):
        if dist[i][j] > dist[i][k] + dist[k][j]:
          dist[i][j] = dist[i][k] + dist[k][j]
  return dist
