#DFS
n, c = list(map(int,input().split()))

graph = [[] for _ in range(n)]

for _ in range(c):
  u, v = map(int, input().split()) 
  graph[u].append(v)
  graph[v].append(u)

def dfs(graph):
  stack = [0]
  visited = []
  while stack:
    atual = stack.pop()
    if atual not in visited:
      visited.append(atual)
      for neighbor in graph[atual]:
        if neighbor not in visited:
          stack.append(neighbor)
  return visited
print(dfs(graph))

