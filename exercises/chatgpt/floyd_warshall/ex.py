n,m = map(int,input().split())
grafo = []
for _ in range(m):
  u,v,w = map(int,input().split())
  grafo.append((u-1,v-1,w))
a,b = map(int,input().split())
def floyd(grafo,n):
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

res = floyd(grafo,n)
final = res[a-1][b-1]
if final != float('inf'):
  print(res[a-1][b-1])
else:
  print("INFINITY")