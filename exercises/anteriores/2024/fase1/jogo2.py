#se 0, 3 vizinhas 1, = 1
#se 0, != 3 vizinhas, = 0
#se 1, 2/3 vizinhas 1, = 1
#se 1, < 2 vizinhas 1, = 0
#se 1, > 3 vizinhas 1, = 0

#N e Q - numero de linhas/colunas, numero de passos a serem simulados
#

def calcular_vizinhos_vivos(matriz, i, j, n):
  directions = [(0,1), (0,-1), (-1,0), (1,0), (-1,-1), (1,1), (1,-1), (-1,1)]
  vizinhos_vivos = 0
  for di, dj in directions:
    ni, nj = i+di, j+dj
    if 0 <= ni < n and 0 <= nj < n:
      if matriz[ni][nj] == '1':
        vizinhos_vivos += 1
  return vizinhos_vivos

def calcular_geracao(matriz, n):
  novamatriz = [['0' for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      vizinhos_vivos = calcular_vizinhos_vivos(matriz, i, j, n)
      if matriz[i][j] == '1':
        if vizinhos_vivos < 2 or vizinhos_vivos > 3:
          novamatriz[i][j] = '0'
        else:
          novamatriz[i][j] = '1'
      else:
        if vizinhos_vivos == 3:
          novamatriz[i][j] = '1'
        else:
          novamatriz[i][j] = '0'
  return novamatriz
        
def simular(matriz,n,q):
  for _ in range(q):
    matriz = calcular_geracao(matriz, n)
  return matriz
  
n, q = map(int, input().split())
matriz = []
for i in range(n):
  matriz.append(input())

res = simular(matriz, n, q)
print("-----")
for linhas in res:
  print("".join(linhas))


