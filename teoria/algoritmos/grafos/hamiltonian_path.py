def hamiltonian(grafo):
  n = len(grafo)
  visited = [False] * n

  def backtrack(vertex, count):
    if count == n:
      return True
    for neighbor in range(n):
      if grafo[vertex][neighbor] == 1 and not visited[neighbor]:
        visited[neighbor] = True
        if backtrack(neighbor, count+1):
          return True
        visited[neighbor] = False
    return False
  
  for start in range(n):
    visited[start] = True
    if backtrack(start, 1):
      return True
    visited[start] = False

  return False