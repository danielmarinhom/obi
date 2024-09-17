#N computadores - M conexoes
#U e V - conexao bidirecional entre os computadores U e V
#S nodulo inicial

n, m = list(map(int, input().split()))
conexoes = [(list(map(int, input("").split()))) for _ in range(m)]
s = int(input(""))

def bfs(grafo, s, n):
  visited = [(s)]
  queue = [(s, 0)]
  while queue:
    atual, distancia = queue.pop(0)
    if atual == n:
      return distancia
    if 0 <= atual <= n and atual not in visited:
      for i in range(grafo):
        for j in range(grafo[i]):
          if (atual, atual+1) in grafo: 
            atual += 1
            visited.append((atual))
            queue.add((atual, distancia+1))
  return -1

print(bfs(conexoes, s, n))