def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]

def union(a, b):
  rootA = find(a)
  rootB = find(b)
  if rootA != rootB:
    if rootA > rootB:
      parent[rootB] = rootA
    else:
      parent[rootA] = rootB

def kruskal(num_vertices, edges):
  edges.sort(key=lambda x: x[2])
  mst = []
  mst_weight = 0
  for u, v, weight in edges:
    if find(u) != find(v):
      union(u, v)
      mst.append((u, v))
      mst_weight += weight
      if len(mst) == num_vertices - 1:
        break
  return mst_weight

n, m = map(int,input().split())
parent = [i for i in range(n)]
edges = []

for _ in range(m):
  u,v,w = map(int,input().split())
  edges.append((u,v,w))

print(kruskal(n, edges))