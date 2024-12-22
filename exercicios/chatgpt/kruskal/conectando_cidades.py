#N, M - numero de cidades
#M linhas, U, V, W - U, V cidades que podem ser conectadas, W o custo

#Custo total minimo para conectar todas as cidades
import time
start_time = time.time()
def find(p):
  if parent[p] != parent[p]:
    parent[p] = find(parent[p])
  return parent[p]

def union(a, b):
  paiA = find(a)
  paiB = find(b)
  
  if paiA != paiB:
    if paiA > paiB:
      parent[paiB] = paiA
    else:
      parent[paiA] = paiB
  
def kruskal(edges, num_vertices):
  edges.sort(key=lambda x:x[2])
  mst = []
  mst_weight = 0

  for u, v, weight in edges:
    if find(u) != find(v):
      union(u,v)
      mst.append((u,v))
      mst_weight += weight
      if len(mst) == num_vertices - 1:
        break
  return mst_weight


n, m = map(int, input().split())
parent = [i for i in range(n)]
edges = []
for _ in range(m):
  u, v, w = map(int, input().split())
  edges.append((u,v,w))

print(kruskal(edges, m))
print("Process finished --- %s seconds ---" % (time.time() - start_time))