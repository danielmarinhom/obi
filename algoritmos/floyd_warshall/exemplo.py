n = int(input())
m = int(input())
grafo = [[] for _ in range(n)]

for _ in range(m):
  u,v,t = map(int,input().split())
  grafo[u-1].append((v-1, t))

def floyd(grafo,n):
  dist = [[float('inf')] * n for _ in range(n)]
  for i in range(n):
    grafo[i][i] = 0
  for i in range(n):
    for j in grafo[u]:
      if i == j:
        grafo[i][j] = 0
      elif grafo[i][j] != 0:
        dist[i][j] = grafo[i][j]
  
  for k in range(n):
    for i in range(n):
      for j in range(n):
        if dist[i][j] > dist[i][k]+dist[k][j]:
          dist[i][j] = dist[i][k]+dist[k][j]
  return dist