print(x for x in range(1,9))
n,m = map(int,input().split())
edges = []
for _ in range(m):
  u,v = map(int,input().split())
  edges.append((u-1,v-1))
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
def conexoes(edges):
  vertices = set()
  for u,v in edges:
    vertices.add(u)
    vertices.add(v)
    union(u,v)
  print(vertices)
  pai = find(list(vertices)[0])
  for vertex in vertices:
    if find(vertex) != pai:
      return "Desconectado" 
  return "Conectado"
print(conexoes(edges))
    