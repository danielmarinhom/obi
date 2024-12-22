c,e,l,p = map(int,input().split()) #c - cidades, e - estradas, l - atual, p - maximo
conexoes = []
for _ in range(e):
  x,y = map(int,input().split())
  conexoes.append((x,y))

def bfs(conexoes, atual, maximo):
  queue = [(atual,0)]
  visited = set([atual])
  while queue:
    novo, distancia = queue.pop(0)
    if distancia < maximo:
      for x,y in conexoes:
        if x == novo and y not in visited:
          queue.append((y,distancia+1))
          visited.add(y)
        elif y == novo and x not in visited:
          queue.append((x,distancia+1))
          visited.add(x)
  return sorted(visited - {atual})

respostas = []
while True:
  c,e,l,p = map(int,input().split()) #c - cidades, e - estradas, l - atual, p - maximo
  conexoes = []
  if (c,e,l,p) == (0,0,0,0):
    break
  for _ in range(e):
    x,y = map(int,input().split())
    conexoes.append((x,y)) 
  respostas.append(bfs(conexoes,l,p))
print(respostas)
for i, numero in enumerate(respostas):
  print(f"Teste {i+1}")
  print(" ".join(map(str,numero)))
  print()


