#0 livre, 1 obstaculo

n, m = input().split()
n, m = int(n), int(m)
graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))

def bfs(graph, n, m):
  #esquerda, direita, cima, baixo
  directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  visited = set((0, 0))
  queue = [(0, 0, 0)]
  while queue:
    x, y, distancia = queue.pop(0)

    if x == n-1 and y == m-1:
      return distancia

    for dx, dy in directions:
      ax, ay = x + dx, y + dy
      if (0 <= ax < n and 0 <= ay < m and graph[ax][ay] == 0) and (ax, ay) not in visited:
        visited.add((ax, ay))
        queue.append((ax, ay, distancia+1))
  return -1
  

print(bfs(graph, n, m))