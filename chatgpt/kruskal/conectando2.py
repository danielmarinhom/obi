import timeit
def initialize(size):
    global parent, rank
    parent = [i for i in range(size)]
    rank = [1] * size

def find(p):
    if parent[p] != p:
        parent[p] = find(parent[p])  # Path Compression
    return parent[p]

def union(p, q):
    rootP = find(p)
    rootQ = find(q)

    if rootP != rootQ:
        if rank[rootP] > rank[rootQ]:
            parent[rootQ] = rootP
        elif rank[rootP] < rank[rootQ]:
            parent[rootP] = rootQ
        else:
            parent[rootQ] = rootP
            rank[rootP] += 1

def kruskal(edges, num_vertices):
    # Inicializa a estrutura Union-Find para os vértices
    initialize(num_vertices)
    
    # Ordena as arestas pelo peso
    edges.sort(key=lambda x: x[2])
    
    mst = []
    mst_weight = 0
    
    for u, v, weight in edges:
        # Verifica se u e v estão no mesmo conjunto
        if find(u) != find(v):
            # Se não estiverem, adiciona a aresta à MST e une os conjuntos
            union(u, v)
            mst.append((u, v))
            mst_weight += weight
            
            # Se a MST tiver V-1 arestas, podemos parar
            if len(mst) == num_vertices - 1:
                break
    
    return mst_weight
import timeit
# Exemplo de uso
def run_kruskal():
  num_vertices, num_edges = 4, 5
  edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
  mst_weight = kruskal(edges, num_vertices)
  print(mst_weight)

execution_time = timeit.timeit("run_kruskal()", setup="from __main__ import run_kruskal", number=10000)
execution_time = execution_time / 10000
print(f"Process finished in {execution_time*1000000} MICROSECONDS")

