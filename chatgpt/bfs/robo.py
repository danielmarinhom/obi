#n*n
#0 pode passar
#1 nao pode passar
#cima, baixo esquerda ou direita
#de [0][0] ate [n-1][n-1]

def bfs(graph):
  if graph[0][0] == '1' or graph[n-1][n-1] == '1':
    return -1
  
  directions = [(-1, 0), (1,0), (0, -1), (0, 1)] #cima, baixo, esquerda, direita

  visited = set((0, 0))
  queue = [(0,0,0)] #x, y, distancia percorrida
  
  while queue:
    x, y, distancia = queue.pop(0)
    if x == n-1 and y == n-1:
      return distancia
    
    for dx, dy in directions:
      nx, ny = x + dx, y + dy #nova coordenada
      if (0 <= nx < n and 0 <= ny < n and graph[nx][ny] == '0') and (nx, ny) not in visited: #verifica se esta nos limites da matriz e se eh possivel visitar
        visited.add((nx, ny))
        queue.append((nx, ny, distancia+1))
  return -1

n = int(input(""))
graph = [[0] for _ in range(n)]
for i in range(n):
  graph[i] = input("").split()

#n = int(input())
#graph = [input().split() for _ in range(n)]


print(bfs(graph))