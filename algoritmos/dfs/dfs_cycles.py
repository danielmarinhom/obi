#GRAFO DIRECIONADO

def dfs(grafo, node, visited, parent):
  visited[node] = True
  for neighbor in grafo[node]:
    if not visited[neighbor]:
      if dfs(grafo,neighbor,visited,node):
        return True
    elif neighbor != parent:
      return True
  return False

def detect_cycle(grafo,n):
  visited = [False] * (n+1)
  for node in range(1,n+1):
    if not visited[node]:
      if dfs(grafo,node,visited,-1):
        return True
  return False
#A função dfs detecta ciclos verificando se encontramos um vizinho que já foi visitado e que não é o pai do nó atual. Isso indica a presença de um ciclo porque significa que existe uma aresta que não é parte da árvore de DFS, mas que conecta dois nós na árvore.
n = 6
graph = [[] for _ in range(n + 1)]
edges = [(1, 2), (2, 3), (2, 4), (4, 5), (5, 6)]

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

has_cycle = detect_cycle(graph, n)
print(has_cycle)  # Saída esperada: False (Não há ciclo)

# Adicionando um ciclo
edges = [(1, 2), (2, 3), (2, 4), (3, 4), (4, 5), (5, 6)]

graph = [[] for _ in range(n + 1)]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

has_cycle = detect_cycle(graph, n)
print(has_cycle)  # Saída esperada: True (Há um ciclo 2-3-4)