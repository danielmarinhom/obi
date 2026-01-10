#non-directional graph
def bellman_ford(graph, num_vertices, start):
  dist = [float('inf')] * num_vertices
  dist[start] = 0

  for _ in range(num_vertices-1):
    for u, v, w in graph:
      if dist[u] != float('inf') and dist[u] + w < dist[v]:
        dist[v] = dist[u] + w
      if dist[v] != float('inf') and dist[v] + w < dist[u]:
        dist[u] = dist[v] + w
  #negative cycle verification
  negative = [False]*num_vertices
  for u, v, w in graph:
    if dist[u] != float('inf') and dist[u] + w < dist[v]: 
      print("graph has a w negative cycle")
      negative[v] = True
  #propagation of negative cycles
  for _ in range(num_vertices):
    for u,v,w in graph:
      if negative[u]:
        negative[v] == True
  
  return dist
graph = [(0, 1, -1),
(0, 2, 4),
(1, 2, 3),
(1, 3, 2),
(1, 4, 2),
(3, 2, 5),
(3, 1, 1),
(4, 3, -3)]

data = input().split()
num_vertices = int(data[0])
num_edges = int(data[1])

edges = []
index = 2
for _ in range(num_edges):
  u = int(data[index])
  v = int(data[index+1])
  weight = int(data[index+2])
  edges.append((u,v,weight))
  index+=3
  result = bellman_ford(edges, num_vertices, 0)    
  if result:
    for dist in result:
      if dist == float('inf'):
        print("INF", end=' ')
      else:
        print(dist, end=' ')
    print()