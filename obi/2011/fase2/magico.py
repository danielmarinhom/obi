#soma dos nnumeros em uma linha, coluna ou diagonal principal tenham o mesmo valor
#ordem eh o numero de lihas, valor eh o resultado da soma de uma linha

n = int(input())
matriz = []
for _ in range(n):
  matriz.append(list(map(int,input().split())))

def magico(matriz,n):
  #soma dos N numeros em uma linha, coluna ou ii tenham sempre o mesmo valor
  #diagonal
  sd = 0
  for i in range(n):
    sd += matriz[i][i]
  #linhas
  sl = sum(matriz[i])
  for i in range(n):
    atual = sum(matriz[i])
    if atual != sl:
      return 0
    
  res = []
  for i in range(n):
    soma = 0
    i = 0
    for j in range(n):
      soma += matriz[i][j] 
      i += 1
    res.append(soma)
  for elemento in res:
    if res.count(elemento) != len(res):
      return 0
  return sl
print(magico(matriz,n))