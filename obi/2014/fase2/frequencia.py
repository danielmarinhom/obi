#1XR - atribuir o  valor a todos os numeros da LINHA X
#2XR - atribuir o valor R a todos os numeros da COLUNA X
#3X - imprimir o valor mais frequente na LINHA X
#4X - imprimir o valor mais frequente na COLUNA X

n,q = map(int,input().split()) #NxN, operacoes
grafo = [[0]*n for _ in range(n)]
operacoes = [] #(1,X,R), (3,X)
for _ in range(q):
  operacoes.append(tuple(map(int,input().split())))

for comando in operacoes:
  #UM
  if comando[0] == 1:
    x,r = comando[1],comando[2]
    x-=1
    for i in range(len(grafo[x])):
      grafo[x][i] = r
  #DOIS
  elif comando[0] == 2:
    x,r = comando[1],comando[2]
    x-=1
    for i in range(len(grafo)):
      grafo[i][x] = r
  #TRES
  elif comando[0] == 3:
    x = comando[1]
    x-=1
    vezes = 0
    res = 0
    for valor in grafo[x]:
      if grafo[x].count(valor) >= vezes and valor > res:
        vezes = grafo[x].count(valor)
        res = valor
    print(res)
  #QUATRO
  elif comando[0] == 4:
    x = comando[1]
    x-=1
    vezes = 0
    res = 0
    elementos = [row[x] for row in grafo]
    for elemento in elementos:
      if elementos.count(elemento) >= vezes and elemento > res:
        vezes = elementos.count(elemento)
        res = elemento
    print(res)


