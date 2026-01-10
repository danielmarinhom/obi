#N, M - numero de cidades
#M linhas, U, V, W - U, V cidades que podem ser conectadas, W o custo

#Custo total minimo para conectar todas as cidades
import timeit
def find(p, parent):
  if parent[p] != p:
    parent[p] = find(parent[p], parent)
  return parent[p]

def union(a, b, parent):
  paiA = find(a, parent)
  paiB = find(b, parent)
  
  if paiA != paiB:
    if paiA > paiB:
      parent[paiB] = paiA
    else:
      parent[paiA] = paiB
  
def kruskal(edges, num_vertices, parent):
  edges.sort(key=lambda x:x[2])
  mst = []
  mst_weight = 0

  for u, v, weight in edges:
    if find(u, parent) != find(v, parent):
      union(u,v, parent)
      mst.append((u,v))
      mst_weight += weight
      if len(mst) == num_vertices - 1:
        break
  return mst_weight

def run_kruskal():
  n, m = 4,5
  parent = [i for i in range(n)]
  edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
  print(kruskal(edges, m, parent))

execution_time = timeit.timeit("run_kruskal()", setup="from __main__ import run_kruskal", number=10000)
execution_time = execution_time / 10000
print(f"Process finished in {execution_time*1000000} MICROSECONDS")