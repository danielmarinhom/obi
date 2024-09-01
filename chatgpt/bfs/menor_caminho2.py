n,m = map(int,input().split())
grafo = [list(map(int,input().split())) for _ in range(n)]

def bfs(grafo, n, m):
  if grafo[0][0] == 1 or grafo[n-1][m-1] == 1:
    return -1
  directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] #n s l o
  queue = [(0,0, 1)]
  visited = set()
  while queue:
    x, y, custo = queue.pop(0)
    if x == n-1 and y == m-1:
      return custo
    for dx, dy in directions:
      nx, ny = x+dx, y+dy
      if 0 <= nx < n and 0 <= ny < m and grafo[nx][ny] == 0 and (nx,ny) not in visited:
        queue.append((nx,ny, custo+1))
        visited.add((nx,ny))
  return -1
print(bfs(grafo,n, m))