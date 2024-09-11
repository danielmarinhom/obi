#caminho mais curto entre arestas ponderadas (podem ser negativas)
#grafo direcionado (unilateral)
def bellman_ford(grafo, num_vertices, inicio):
  distancia = [float('inf')] * num_vertices
  distancia[inicio] = 0

  for _ in range(num_vertices-1):
    for u, v, peso in grafo:
      if distancia[u] != float('inf') and distancia[u] + peso < distancia[v]:
        distancia[v] = distancia[u] + peso
  #verificacao de ciclo negativo
  ciclo_negativo = [False]*num_vertices
  for u, v, peso in grafo:
    if distancia[u] != float('inf') and distancia[u] + peso < distancia[v]: 
      print("o grafo contem um ciclo de peso negativo")
      ciclo_negativo[v] = True
  #propagacao dos ciclos negativos
  for _ in range(num_vertices):
    for u,v,peso in grafo:
      if ciclo_negativo[u]:
        ciclo_negativo[v] == True
  
  return distancia
grafo = [(0, 1, -1),
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