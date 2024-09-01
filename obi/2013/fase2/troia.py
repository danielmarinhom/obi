#cada item indicavam duas pessoas que pertenciam a uma mesma familia

#N - numero de elementos da comunidade de 1 a N
#M linhas, 2 inteiros, cada inteiro identifica um elemento da comunidade
#cada linha indica que os dois individuos pertencem a uma mesma familia

#numero de familias
def calcular_familias(n, relacoes):
  grafo = [[] for _ in range(n+1)]
  for u, v in relacoes:
    familias[u].append(v)
    familias[v].append(u)

    visited = [False] * (n + 1)
    familias = 0
  def dfs(node, visited):
    stack = [node]
    while stack:
      atual = stack.pop(0)
      for vizinho in grafo[atual]:
        if not visited[vizinho]:
          visited[vizinho] = True
          stack.append(vizinho)
  for i in range(1,n+1):
    if not visited[i]:
      familias += 1
      visited[i] = True
      dfs(i, visited)
    
data = input().split()
N = int(data[0])
M = int(data[1])
relacoes = [(int(data[i]), int(data[i+1])) for i in range(2, len(data), 2)]

print(calcular_familias(N, relacoes))
