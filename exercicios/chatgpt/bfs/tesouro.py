#. (terra)
#T (arvore) 
#R (rio)
#comeca no S termina no E
#norte sul leste oeste

n,m = map(int,input().split())
grafo = []
for _ in range(n):
  grafo.append(input().strip())

def get_s(grafo):
  for i in range(len(grafo)):
    for j in range(len(grafo[0])):
      if grafo[i][j] == 'S':
        return i,j
def bfs(grafo,n,m,x,y):
  queue = [(x,y,0)]
  visited = set([(x,y)])
  directions = [(0,-1),(0,1),(1,0),(-1,0)]
  while queue:
    x,y,dist = queue.pop(0)
    if grafo[x][y] == 'E':
      return dist
    for dx, dy in directions:
      nx, ny = x+dx, y+dy
      if 0 <= nx < n and 0 <= ny < m and (nx,ny) not in visited:
        if grafo[nx][ny] != 'R':
          queue.append((nx,ny,dist+1))
          visited.add((nx,ny))
  return -1
x,y = get_s(grafo)
print(bfs(grafo,n,m,x,y))