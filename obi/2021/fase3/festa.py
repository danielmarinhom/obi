n = int(input()) # numero de suditos
m = int(input()) # turnos
suditos = [i for i in range(1,n+1)]
sorteados = []
for _ in range(m):
  sorteados.append(int(input()))

for i in range(m):
  for j in range(1,len(suditos)):
    if sorteados[i] % j == 0:
      suditos.pop(j)

for i in range(len(suditos)):
  print(suditos[i])
