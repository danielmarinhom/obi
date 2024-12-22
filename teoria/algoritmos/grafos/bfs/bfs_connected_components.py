def bfs(graph, start, visited, component):
  queue = [start]
  visited[start] = True
  while queue:
    node = queue.pop(0)
    component.append(node)
    for neighbor in graph[node]:
      if not visited[neighbor]:
        visited[neighbor] = True
        queue.append(neighbor)
def find_connected(graph,n):
  visited = [False] * (n+1)
  components = []
  for node in range(1,n+1):
    if not visited[node]:
      component = []
      bfs(graph,node,visited,component)
      components.add(component)
  return components