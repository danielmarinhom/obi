n, m = list(map(int, input().split()))
conexoes = []
for i in range(m):
  conexoes.append(list(map(int,input().split())))

grafo = [[] for _ in range(n+1)]
for x, y in conexoes:
  grafo[x].append(y)
  grafo[y].append(y)

visited = [False] * (n+1)

def dfs(n, visited,grafo):
  stack = [n]
  while stack:
    atual = stack.pop()
    if not visited[atual]:
      visited[atual] = True
      for vizinho in grafo[atual]:
        if not visited[vizinho]:
          stack.append(vizinho)  

res = 0

for i in range(1,n+1):
  if not visited[i]:
    res += 1
    dfs(i, visited, grafo)
print(res)