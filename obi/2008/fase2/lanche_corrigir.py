#distancia entre a cozinha e a sala mais distante da cozinha seja a menor possivel

#S e C - numero de salas, numero de corredores
#C linhas seguintes ccontem, A, B e D - existe um corredor de D metros ligando A e B
#DJIKSTRA
s,c = map(int,input().split())
conexoes = []
for _ in range(c):
  a,b,d = map(int,input().split())
  conexoes.append((a,b,d))

parent = [i for i in range(s)]

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

print(kruskal(conexoes, s))