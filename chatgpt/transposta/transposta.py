tamanhos = input("").split()
n, m = int(tamanhos[0]), int(tamanhos[1])
matriz = [[0]*m for _ in range(n)]

for i in range(n):
  l = input("").split()
  for j in range(m):
    matriz[i][j] = l[j]


transposta = [[0]*n for _ in range(m)]

for i in range(n):
  for j in range(m):
    transposta[j][i] = matriz[i][j]


for i in range(m):
    for j in range(n):
        if j != n - 1:
            print(transposta[i][j], end=" ")
        else:
            print(transposta[i][j])
