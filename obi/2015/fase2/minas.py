n = int(input())

grafo = []
for i in range(n):
  grafo.append(list(map(int, input().split())))

def bfs(grafo, n):
  stack = [(0, 0, 0)] #x, y, quantidade de pedras
  direcoes = [(0,-1), (0,1), (-1,0), (1,0)] #cima, baixo, esquerda, direita
  visited = [[False]*n for _ in range(n)]
  visited[0][0] = True
  while stack:
    x, y, qtd = stack.pop(0)

    if x == n-1 and y == n-1:
      return qtd

    for dx, dy in direcoes:
      nx, ny = x+dx, y+dy
      if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
        visited[nx][ny] = True
        if grafo[nx][ny] == 1:
          stack.append((nx, ny,qtd+1))
        else:
          stack.append((nx, ny,qtd))
  return 0
print(bfs(grafo, n))
    