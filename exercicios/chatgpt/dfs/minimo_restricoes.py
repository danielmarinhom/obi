n = int(input())
m = int(input())
edges = []
for _ in range(m):
  u,v,w = map(int,input().split())
  edges.append((u,v,w))
r = int(input())
restritos = []
for _ in range(r):
  restritos.append(int(input()))
s, t = map(int,input().split())

def dfs(grafo, atual, destino, restritos, visitados, peso_atual):
  if atual == destino:
    return peso_atual
  visitados[atual] = True
  peso_minimo = float('inf')
  for vizinho, peso in grafo[atual]:
    if not visitados[vizinho] and vizinho not in restritos:
      resultado = dfs(grafo,vizinho,destino,restritos,visitados,peso_atual + peso)
      if resultado != -1:
        peso_minimo = min(peso_minimo, resultado)
  return peso_minimo if peso_minimo != float('inf') else -1

def caminho_minimo(n, edges, restritos, s,t):
  grafo = [[] for _ in range(n+1)]
  for u,v,w in edges:
    grafo[u].append((v,w))
    grafo[v].append((u,w))
  visitados = [False]*(n+1)
  return dfs(grafo,s,t,restritos,visitados,0)
print(caminho_minimo(n,edges,restritos,s,t))
