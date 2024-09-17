n,m = map(int,input().split())
conexoes = []

edges = [[] for _ in range(n)]
for _ in range(m):
  u,v,c = map(int,input().split())
  conexoes.append((u-1,v-1,c))
  edges[u-1].append((v-1,c))
  edges[v-1].append((u-1,c))
s,t = map(int,input().split()) #start, ending
s -= 1  #zero index
t -= 1

def bfs_acessible(comeco, fim,num_vertices,grafo):
  queue = [comeco]
  visited = [False] * num_vertices
  visited[comeco] = True
  while queue:
    node = queue.pop(0)
    if node == fim:
      return True
    for neighbor,_ in grafo[node]:
      if not visited[neighbor]:
        visited[neighbor] = True
        queue.append(neighbor)
  return False


def bellman_ford(grafo, comeco, fim, num_vertices, visited):
  dist = [float('inf')] * num_vertices
  dist[comeco] = 0
  for _ in range(num_vertices-1):
    for u,v,w in grafo:
      if visited[u] and visited[v] and w >= 0 and dist[u] != float('inf') and dist[u] + w < dist[v]:
        dist[v] = dist[u] + w
  return dist[fim] if dist[fim] != float('inf') else -1

visited = bfs_acessible(s,t,n,edges)
print(bellman_ford(conexoes, s, t, n, visited))