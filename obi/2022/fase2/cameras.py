#K linhas seguintes, Ci, Li, Di - coluna, linha e a direcao
#N,S,L,O
n,m,k = map(int,input().split()) #linhas, colunas e cameras
norte, sul, leste, oeste = 0, m-1, n-1, 0
grafo = [[0]*m for _ in range(n)]
cameras = []
for _ in range(k):
  c, l, d = input().split()
  c,l = int(c)-1, int(l)-1
  cameras.append((c,l,d))

#preencher grafo com 1's
for x,y,d in cameras:
  if d == 'N':
    for i in range(x, norte-1, -1):
      grafo[i][y] = 1
  if d == 'S':
    for i in range(x, sul+1):
      grafo[i][y] = 1
  if d == 'L':
    for i in range(y, leste+1):
      grafo[x][i] = 1
  if d == 'O':
    for i in range(y, oeste-1, -1): 
      grafo[x][i] = 1
def bfs(grafo):
  rows, cols = len(grafo), len(grafo[0])
  queue = [(0,0)] #x,y
  directions = [(0,-1),(0,1),(1,0),(-1,0)]
  visited = set()
  visited.add((0,0))
  while queue:
    x, y = queue.pop(0)
    if (x,y) == (rows-1, cols-1):
        return "S"
    for dx,dy in directions:
      nx,ny = x+dx, y+dy
      if 0 <= nx < rows and 0 <= ny < cols and (nx,ny) not in visited and grafo[nx][ny] == 0:
        visited.add((nx,ny))
        queue.append((nx,ny))
  return "N"

print(bfs(grafo))


