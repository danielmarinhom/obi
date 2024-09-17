n,m,r = map(int,input().split())
edges = []
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

for _ in range(m):
  u,v = map(int,input().split())
  edges.append((u-1,v-1))

inimigas = []
for _ in range(r):
  x, y = map(int,input().split())
  inimigas.append((x-1,y-1))

for u,v in edges:
  if (u,v) not in inimigas and (v,u) not in inimigas:
    union(u,v)
componentes = set(find(i) for i in range(n))
print(len(componentes))
