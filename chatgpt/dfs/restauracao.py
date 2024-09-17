n,m = map(int,input().split())
conexoes = []
for _ in range(m):
  u,v = map(int,input().split())
  conexoes.append((u,v))
x = int(input())

def dfs(grafo,visited, node):
  stack = [node]
  while stack:
    current = stack.pop()
    for neighbor in grafo[current]:
      if not visited[neighbor]:
        stack.append(neighbor)
        visited[neighbor] = True
def min_connections(n,m,conexoes, infected):
  grafo = [[] for _ in range(n+1)]
  for u,v in conexoes:
    grafo[u].append(v)
    grafo[v].append(u)
  visited = [False]*(n+1)
  visited[infected] = True
  componentes = 0