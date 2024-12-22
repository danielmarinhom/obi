n = int(input())
grafo = []
for _ in range(n):
  grafo.append(list(map(int,input().split())))
def hamiltonian(grafo):
  n = len(grafo)
  visited = [False] * n
  def backtracking(vertex, count):
    if count == n:
      return True
    for neighbor in range(n):
      if grafo[vertex][neighbor] == 1 and not visited[neighbor]:
        visited[neighbor] = True
        if backtracking(neighbor, count+1):
          return True
        visited[neighbor] = False
    return False
  for i in range(n):
    visited[i] = True
    if backtracking(i, 1):
      return True
    visited[i] = False
  return False
x = hamiltonian(grafo)
print("YES" if x else "NO")