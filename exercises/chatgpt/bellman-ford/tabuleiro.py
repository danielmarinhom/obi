
v,e = map(int,input().split()) #vertices, arestas
edges = []
for _ in range(e):
  u,v,w = map(int,input().split())
  edges.append((u-1,v-1,w))
s = int(input())-1 #start

def bellman_ford(edges, num_vertices,start):
  dist = [float('inf')] * num_vertices
  dist[start] = 0
  for _ in range(num_vertices-1):
    for u,v,w in edges:
      if u < num_vertices and v < num_vertices:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
          dist[v] = dist[u] + w

  for u,v,w in edges:
    if u < num_vertices and v < num_vertices:
      if dist[u] != float('inf') and dist[u] + w < dist[v]:
        return -1
  
  res = ' '.join(str(d) if d != float('inf') else '-1' for d in dist)
  return res

print(bellman_ford(edges,v,s))