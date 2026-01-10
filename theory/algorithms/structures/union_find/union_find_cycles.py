#PARA GRAFOS NAO DIRECIONADOS
n = 7
parent = [i for i in range(n)]
def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]
def union(a,b):
  rootA = find(a)
  rootB = find(b)
  if rootA != rootB:
    if rootA > rootB:
      parent[rootB] = rootA
    else:
      parent[rootA] = rootB
  else:
    return "CYCLE DETECTED"
def detect_cycle(edges):
  for u,v in edges:
    if union(u,v) == "CYCLE DETECTED":
      return True
  return False