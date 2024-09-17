def soma_diagonal(matriz, n):
  resultado = []
  for i in range(n):
    atual = int(matriz[i][n-1 - i])
    resultado.append(atual)
  return sum(resultado)

n = int(input(""))
linhas = [input("") for _ in range(n)]
matriz = []
for i in range(n):
  matriz.append(linhas[i].split())

print(soma_diagonal(matriz, n))

