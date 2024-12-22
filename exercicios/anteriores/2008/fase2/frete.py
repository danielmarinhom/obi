#3 minutos e 28 segundos
n,m = map(int,input().split())
conexoes = []
for _ in range(m):
  p,q,u = map(int,input().split())
  conexoes.append((p,q,u))
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
def kruskal(edges, num_vertices):
  edges.sort(key=lambda x: x[2])
  mst, mst_weight = [], 0
  for u,v,w in edges:
    if find(u) != find(v):
      union(u,v)
      mst.append((u,v,w))
      mst_weight += w
      if len(mst) == num_vertices-1:
        break
  return mst_weight

print(kruskal(conexoes,n))
