n,m = map(int,input().split())
edges = []
for _ in range(m):
  u,v,w = map(int,input().split())
  edges.append((u-1,v-1,w))
parent = [i for i in range(n)]

def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]
def union(a,b):
  rootA = find(a)
  rootB = find(b)
  if rootA != rootB:
    parent[rootB] = rootA
  else:
    parent[rootA] = rootB

def kruskal(edges, n):
  edges.sort(key = lambda x: x[2])
  mst, mst_w = [], 0
  for u,v,w in edges:
    if find(u) != find(v):
      union(u,v)
      mst.append((u,v))
      mst_w += w
      if len(mst) == n-1:
        break
  return mst_w

print(kruskal(edges,n))
