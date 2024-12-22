# leitura  

# dfs 
# transpose
# dfs2  
# sccs  
# mapeamento 

n,m = map(int,input().split())
grafo = [[] for _ in range(n+1)]
for _ in range(m):
  u,v = map(int,input().split())
  grafo[u].append(v)

def dfs1(grafo, node, stack, visited):
  visited[node] = True
  for neighbor in grafo[node]:
    if not visited[neighbor]:
      dfs1(grafo, neighbor, stack, visited)
  stack.append(node)

def transpose(grafo, n):
  transposed = [[] for _ in range(n+1)]
  for _ in range(1, n+1):
    for v in grafo[u]:
      transposed[v] = u
  return transposed

def dfs2(grafo, node, components, visited):
  visited[node] = True
  components.append(node)
  for neighbor in grafo[node]:
    if not visited[neighbor]:
      dfs2(grafo, neighbor, components, visited)

def sccs(grafo, n):
  stack = []
  visited = [False] * (n+1)
  for node in range(1, n+1):
    dfs1(grafo, node, stack, visited)
  
  visited = [False] * (n+1)
  sccs = []
  while stack:
    node = stack.pop()
    if not visited[node]:
      components = []
      dfs2(grafo, node, components, visited)
      sccs.append(components)
  return sccs
sccs = sccs(grafo, n)

sccs_map = {}
for i, component in enumerate(sccs):
  for node in component:
    sccs_map[node] = i
condensed = [[] for _ in range(len(sccs))]
in_degree = [0] * len(sccs)
out_degree = [0] * len(sccs)

for node in range(1, n+1):
  for connection in grafo[node]:
    if sccs_map[node] != sccs_map[connection]:
      condensed[sccs_map[node]].append(sccs_map[connection])
      in_degree[sccs_map[connection]] += 1
      out_degree[sccs_map[node]] += 1
sources = sum(1 for x in in_degree if x == 0)
ends = sum(1 for x in out_degree if x == 0)
print(max(sources, ends))