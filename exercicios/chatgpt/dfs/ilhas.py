#1 terra
#0 agua
#numero de ilhas
l = input("").split()
n, m = list(map(int,l))
graph = []
for i in range(n):
  linha = input()
  graph.append(linha.split())
def count_island(graph, n, m):
  def dfs(x,y):
    directions = [(0,1), (0,-1), (-1,0), (1,0)]
    stack = set([x,y])
    while stack:
      x, y = stack.pop(0)
      for dx, dy in directions:
        ax, ay = x+dx, y+dy
      if 0 <= ax < n and 0 <= ay < m and graph[ax][ay] == '1':
        graph[ax][ay] = '0'
        stack.append((ax, ay))
  islands = 0
  for i in range(n):
    for j in range(m):
      if graph[i][j] == '1':
        islands += 1
        dfs(i, j)
  return islands


