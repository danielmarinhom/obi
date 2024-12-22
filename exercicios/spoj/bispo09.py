#L por C, Q - consultas
from numpy import double


l, c, q = map(int,input().split())
consultar = []
for _ in range(q):
  x,y = map(int,input().split())
  consultar.append((x,y))

def bfs(l,c):
  matriz = [[0]*c for _ in range(l)]
  directions = [(1,1),(1,-1),(-1,-1),(-1,1)]
  queue = [(0,0)]
  visit = [[False]*c for _ in range(l)]
  number = 0
  while queue:
    x, y = queue.pop(0)
    matriz[x][y].append(number)
    number += 1
    for dx, dy in directions:
      nx, ny = x+dx, y+dy
      while 0 <= nx < l and 0 <= ny < c:
        if not visit[nx][ny]:
          visit[nx][ny] = True
          queue.append((nx,ny))
        nx += dx
        ny += dy
  return matriz

def queries(matriz, queries):
  results = []
  for x, y in queries:
    x -=1
    y -=1
    double