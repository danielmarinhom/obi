#analisar componente que se for removido aumenta o numero de sccs (componente critico)
n,m = map(int,input().split())
grafo = [[] for _ in range(n+1)]
for _ in range(m):
  u,v = map(int,input().split())
  grafo[u].append(v)
#1 a n
def dfs1(grafo, node, stack, visited):
  visited[node] = True
  for neighbor in grafo[node]:
    if not visited[neighbor]:
      dfs1(grafo, neighbor, stack, visited)
  stack.append(node)

def transposeGraph(grafo, n):
  transposed = [[] for _ in range(n+1)]
  for u in range(1, n+1):
    for v in grafo[u]:
      transposed[v].append(u)
  return transposed

def dfs2(grafo, node, visited, component):
  visited[node] = True
  component.append(node)
  for neighbor in grafo[node]:
    if not visited[neighbor]:
      dfs2(grafo, neighbor, visited, component)

def sccs(grafo, n):
  visited = [False] * (n+1)
  stack = []
  for node in range(1, n+1):
    if not visited[node]:
      dfs1(grafo, node, stack, visited)
  
  transposed = transposeGraph(grafo, n)

  visited = [False] * (n+1)
  sccs = []
  while stack:
    node = stack.pop()
    if not visited[node]:
      components = []
      dfs2(transposed, node, visited, components)
      sccs.append(components)
  return sccs
sccs = sccs(grafo, n)

#mapeamento para transformar cada scc em um vertex
scc_map = {}
for i, component in enumerate(sccs):
  for node in component:
    scc_map[node] = i
#grafo condensado (junta os sccs com edges)
condensed = [[] for _ in range(len(sccs))]
#in degree - quantos nos eh acessado por  #out degree - quantos nos ele acessa
in_degree = [0] * len(sccs)
out_degree = [0] * len(sccs)

for node in range(1,n+1):
  for connection in grafo[node]:
    if scc_map[node] != scc_map[connection]:
      condensed[scc_map[node]].append(scc_map[connection])
      in_degree[scc_map[connection]] += 1
      out_degree[scc_map[node]] += 1
sources = sum(1 for x in in_degree if x == 0)
ends = sum(1 for x in out_degree if x == 0)
print(max(sources, ends))
