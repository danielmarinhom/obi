def dfs(graph, vertex, visited, stack):
  visited[vertex] = True
  for neighbor, weight in graph[vertex]:
    if not visited[neighbor]:
      dfs(graph,neighbor,visited,stack)
  stack.append(vertex) #

def find_topological_order(graph, num_vertices):
  visited = [False]*num_vertices
  stack = []
  for vertex in range(num_vertices):
    if not visited[vertex]:
      dfs(graph, vertex, visited, stack)
  stack.reverse() #reversing to get the topological order
  return stack
def find_longest_path(graph, num_vertices, start):
  top_order = find_topological_order(graph,num_vertices)
  dist = [float('-inf')] * num_vertices
  dist[start] = 0

  for u in top_order:

    if dist[u] != float('-inf'):
      for v, weight in graph[u]: 
        if dist[v] < dist[u] + weight: #
          dist[v] = dist[u] + weight
  return dist
