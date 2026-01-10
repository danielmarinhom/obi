def initialize(size):
    global parent, rank
    parent = [i for i in range(size)]
    rank = [1] * size

def find(p):
    if parent[p] != p:
        parent[p] = find(parent[p]) 
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
    initialize(num_vertices)
    list.sort()
    edges.sort(key=lambda x: x[2])
    
    mst = []
    mst_weight = 0
    
    for u, v, weight in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, weight))
            mst_weight += weight
            
            if len(mst) == num_vertices - 1:
                break
    
    return mst, mst_weight

num_vertices = 4
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

mst, mst_weight = kruskal(edges, num_vertices)
print(mst)
print(mst_weight)
