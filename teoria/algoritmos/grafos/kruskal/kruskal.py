#o kruskal eh usado para achar a minima arvore geradora para verificar parentesco entre vertices
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
        if rootP > rootQ:
            parent[rootQ] = rootP
        else:
            parent[rootP] = rootQ

def kruskal(edges, num_vertices):
    # Inicializa a estrutura Union-Find para os vértices
    initialize(num_vertices)
    list.sort()
    # Ordena as arestas pelo peso
    edges.sort(key=lambda x: x[2])
    
    mst = []
    mst_weight = 0
    
    for u, v, weight in edges:
        # Verifica se u e v estão no mesmo conjunto
        if find(u) != find(v):
            # Se não estiverem, adiciona a aresta à MST e une os conjuntos
            union(u, v)
            mst.append((u, v, weight))
            mst_weight += weight
            
            # Se a MST tiver V-1 arestas, podemos parar
            if len(mst) == num_vertices - 1:
                break
    
    return mst, mst_weight

# Exemplo de uso
num_vertices = 4
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

mst, mst_weight = kruskal(edges, num_vertices)
print("Arestas da MST:", mst)
print("Peso total da MST:", mst_weight)
