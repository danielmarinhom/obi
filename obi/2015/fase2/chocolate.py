#

#X, Y

n = int(input())

matriz = [[0] * n for _ in range(n)]
for i in range(2):
  x, y = list(map(int, input().split()))
  matriz[x-1][y-1] = 1

def verificar_divisao(matriz, n):
  posicao = []
  for i in range(n):
    for j in range(n):
      if matriz[i][j] == 1:
        posicao.append([i, j])
  return abs(posicao[0][0] - posicao[1][0]) > 1

print(verificar_divisao(matriz, n))

