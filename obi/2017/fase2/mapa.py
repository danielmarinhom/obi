#determinar onde hermione se encontra
#l linhas e c colunas
#. ou o

l, c = map(int,input().split())
grafo = []
for _ in range(l):
  grafo.append(input().strip())
print(grafo)

def bfs(grafo, start):
  l, c = len(grafo), len(grafo[0])
  queue = [start]
  visited = set([start])
  directions = [(0,-1),(0,1),(1,0),(-1,0)]#norte,sul,leste,oeste
  while queue:
    x,y = queue.pop(0)
    for dx, dy in directions:
      nx, ny = x+dx, y+dy
      if 0 <= nx < l and 0 <= ny < c and (nx,ny) not in visited and grafo[nx][ny] == 'H':
        visited.add((nx,ny))
        queue.append((nx,ny))
  return x+1, y+1

start = (0,0)
for i in range(len(grafo)):
  for j in range(len(grafo[i])):
    if grafo[i][j] == 'o':
      start = (i,j)
      break
  if start != (0,0):
    break


print(bfs(grafo, start))

#14 min #com chat