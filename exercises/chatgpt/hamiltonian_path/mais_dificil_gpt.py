n = int(input())
start, end = map(int,input().split())
start -= 1
end -= 1
grafo = []
for _ in range(n):
  grafo.append(list(map(int,input().split())))

def hamiltonian(grafo, start, end, n):
  visited = [False] * n
  def backtrack(vertex, count):
    if count == n:
      return vertex == end
    for neighbor in range(n):
      if grafo[vertex][neighbor] == 1 and visited[neighbor] == False:
        visited[neighbor] = True
        if backtrack(neighbor, count+1):
          return True
        visited[neighbor] = False
    return False
  visited[start] = True
  return backtrack(start, 1)

print("YES" if hamiltonian(grafo, start, end, n) else "NO")