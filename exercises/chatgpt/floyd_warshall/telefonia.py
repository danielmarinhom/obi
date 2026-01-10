n,m = map(int,input().split())
edges = []
for _ in range(m):
  u,v,w = map(int,input().split())
  edges.append((u-1,v-1,w))

  def floyd(edges, n):
    dist = [[float('inf')]*n for _ in range(n)]
    for i in range(n):
      dist[i][i] = 0
    for u,v,w in edges:
      dist[u][v] = w
    for k in range(n):
      for i in range(n):
        for j in range(n):
          if dist[i][j] > dist[i][k] + dist[k][j]:
            dist[i][j] = dist[i][k] + dist[k][j]
    return dist
v = floyd(edges, n)
for x in v:
  print("".join(str(x)))
start, end = map(int,input().split())
print(v[start-1][end-1])