#calcular vizinhos
#calcular geracoes
#simular geracoes q vezes

def calcular_vizinhos_vivos(matriz, x, y, n):
  directions = [(0,1), (0,-1), (-1,0), (1,0), (-1,-1), (1,1), (1,-1), (-1,1)]
  vizinhos_vivos = 0
  for dx, dy in directions:
    nx, ny = x+dx, y+dy
    if 0 <= nx < n and 0 <= ny < n:
      if matriz[nx][ny] == '1':
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

def simular_geracoes(matriz, q, n):
  for _ in range(q):
    matriz = calcular_geracao(matriz, n)
  return matriz

n, q = map(int, input().split())
matriz = []
for i in range(n):
  matriz.append(input())

res = simular_geracoes(matriz, q, n)
print("-----")
for linhas in res:
  print("".join(linhas))
