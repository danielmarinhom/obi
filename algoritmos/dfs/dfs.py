#DFS
n, c = list(map(int,input().split()))

graph = [[] for _ in range(n)]

for _ in range(c):
  u, v = map(int, input().split())  #BILATERAL
  graph[u].append(v)
  graph[v].append(u)

def dfs(graph):
  stack = [0]
  visited = []
  while stack:
    atual = stack.pop()
    if atual not in visited:
      visited.append(atual)
      for vizinho in graph[atual]:
        if vizinho not in visited:
          stack.append(vizinho)
  return visited
print(dfs(graph))

