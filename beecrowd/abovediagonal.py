#S or M, Sum or Average

op = input("")
matriz = [[0]*12 for _ in range(12)]

esquerda, direita, cima, baixo = 0, 12, 0, 12

numeros = []

for i in range(12):
    for k in range(12):
        for j in range(12):
            numeros.append(matriz[i+k][i+k:j])

if op == 'S':         
  print(sum(numeros))
elif op == 'M':
  print(sum(numeros)/len(numeros)) 
