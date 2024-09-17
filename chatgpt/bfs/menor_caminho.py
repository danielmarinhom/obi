n,m = map(int,input().split())
grafo = [list(map(int,input().split())) for _ in range(n)]

def bfs(grafo):
  n,m = len(grafo), len(grafo[0])
  directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] #norte sul leste oeste
  costs = [[float('inf')] *m for _ in range(n)]
  costs[0][0] = grafo[0][0]
  queue = [(0,0)]
  while queue:
    x, y = queue.pop(0)
    for dx, dy in directions:
      nx, ny = x+dx, y+dy
      if 0 <= nx < n and 0 <= ny < m:  
        new_cost = costs[x][y] + grafo[x][y]
        if new_cost < costs[nx][ny]:
          costs[nx][ny] = new_cost
          queue.append((nx,ny))
  return costs[n-1][m-1]