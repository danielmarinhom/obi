#n arvores alinhadas
#iesima arvore tem altura Hi, localizada na posicao Xi
#comeca do 0 ate n
#ay > by

n = int(input())

grafo = []
for i in range(n):
  grafo.append(list(map(int, input().split())))

def pode_pular(grafo, a, b):
  return grafo[a][1] >= grafo[b][1]

def bfs(grafo, n):
  queue = [(0, 0)] #posicao, pulos
  visited = [False]*n 
  visited[0] = True
  while queue:
    posicao, pulos = queue.pop(0)
    if posicao == n-1:
      return pulos
        
    for i in range(posicao + 1, n):
      if not visited[i] and pode_pular(grafo, posicao, i):
        visited[i] = True
        queue.append((i, pulos + 1))
  return -1

print(bfs(grafo, n))
      
