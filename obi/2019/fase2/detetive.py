#E,I,V
#total de eventos, implicacoes, eventos verdadeiros
#se A ocorreu, A eh a causa e B eh a consequencia
#se um evento eh consequencia de pelo menos uma causa, ele so pode ocorrer se pelo menos uma de suas causas ocorrer
#nao existem circulos

e,i,v = map(int,input().split())  #eventos, implicacaoes, verdadeiros
eventos = []
for _ in range(i):
  a,b = map(int,input().split())
  eventos.append((a,b))

verdadeiros = []
x = input()
for numero in x:
  verdadeiros.append(int(x))

def eventos_verdadeiros(verdadeiros, e,v, implicacoes):
  grafo = [[] for _ in range(e+1)]
  for u,v in implicacoes:
    grafo[u].append(v)
  
  queue = verdadeiros[:]
  visited = set(verdadeiros)

  while queue:
    atual = queue.pop(0)
    for vizinho in grafo[atual]:
      if vizinho not in visited:
        visited.add(vizinho)
        print(vizinho, visited)
        queue.append(vizinho)
  return sorted(visited)

print(eventos_verdadeiros(verdadeiros, e, v, eventos))