#n * m
#matriz

#x*y
#matriz

#resultado


tam1 = input("").split()
n, m = int(tam1[0]), int(tam1[1])
matriz1 = [[0]*m for _ in range(n)]

for i in range(n):
  l = input("").split()
  for j in range(m):
    matriz1[i][j] = int(l[j])

tam2 = input("").split()
x, y = int(tam2[0]), int(tam2[1])
matriz2 = [[0]*y for _ in range(x)]

for i in range(x):
  l = input("").split()
  for j in range(y):
    matriz2[i][j] = int(l[j])

novamatriz = []

if m != x:
  raise Exception("MATRIZES INVALIDAS")

def multiplicacao_matricial(matriz1, matriz2):
  n = len(matriz1)    #linhas matriz1
  m = len(matriz1[0]) #colunas matriz1
  p = len(matriz2[0]) #colunas matriz2
  resultado = [[0] * p for _ in range(n)]
  for i in range(n):
    for j in range(p):
      for k in range(m):
        resultado[i][j] += matriz1[i][k]*matriz2[k][j]
  return resultado

print(multiplicacao_matricial(matriz1, matriz2))

