#N < 500 >= 1 e M < 10000 >=1
n, m = map(int,input().split())
if n >= 1000 or n < 2 or m > 10000 or m < 1:
  raise Exception("")

conexoes = []
for _ in range(m):
  u,v,w = map(int,input().split())
  conexoes.append((u,v,w))

parent = [i for i in range(m)]

def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]

def union(a, b):
  rootA, rootB = find(a), find(b)
  if rootA != rootB:
    if rootA > rootB:
      parent[rootB] = rootA
    else:
      parent[rootA] = rootB

  

def kruskal(arestas, qtd_vertices):
  arestas.sort(key=lambda x: x[2])
  mst, mst_weight = [], 0
  for u, v, weight in arestas:
    if find(u) != find(v):
      union(u,v)
      mst.append((u,v,weight))
      mst_weight += weight
      if len(mst) == qtd_vertices-1:
        break
  return mst_weight

print(kruskal(conexoes,n))