n = int(input(""))
linhas = [input() for _ in range(n)]
matriz = []
for i in range(n):
  matriz.append(linhas[i].split())

def rotacionar_matriz(n, matriz):
  novamatriz = [[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      novamatriz[j][n-1-i] = matriz[i][j]
  return novamatriz
print(rotacionar_matriz(n, matriz))