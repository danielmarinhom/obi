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

def kruskal(edges, num_vertices):
  edges.sort(key=lambda x: x[2])
  mst = []
  for u,v,_ in edges:
    if find(u) != find(v):
      union(u,v)
      mst.append((u,v))
      if len(mst) == num_vertices-1:
        break
  return mst

indice = 1
resultados = []

while True:
  n,m = map(int,input().split())  #n - vertices, m - arestas
  if n == 0 and m == 0:
    break
  edges = []
  for _ in range(m):
    u,v,w = map(int,input().split())
    edges.append((u-1,v-1,w))
  parent = [i for i in range(n)]
  res = kruskal(edges,n)
  final = []
  for u,v in sorted(res):
    u,v = u+1, v+1
    res = [u,v]
    res.sort()
    u,v = res
    final.append((u,v))
  resultados.append(final)
for i in range(len(resultados)):
  print(f"Teste {i+1}")
  for u,v in resultados[i]:
    print(f"{u} {v}")
