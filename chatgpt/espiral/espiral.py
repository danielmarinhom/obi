def espiral(n, matriz):
  resultado = []
  cima, esquerda, direita, baixo = 0, 0, n-1, n-1
  while esquerda <= direita and cima <= baixo:
    #esquerda pra direita
    for i in range(esquerda, direita + 1):
      resultado.append(matriz[cima][i])
    cima += 1
    #cima pra baixo
    for i in range(cima, baixo + 1):
      resultado.append(matriz[i][direita])
    direita -= 1
    #direita pra esquerda
    if cima <= baixo:
      for i in range(direita, esquerda-1, -1):
        resultado.append(matriz[baixo][i])
      baixo -= 1

    if esquerda <= direita:
      for i in range(baixo, cima-1, -1):
        resultado.append(matriz[i][esquerda])
      esquerda+=1
  return resultado
  
n = int(input(""))
matriz = []
for i in range(n):
  l1 = input("")
  l = l1.split()
  matriz.append(l)

resultado = espiral(n,matriz)
resultado = " ".join(resultado)
print(resultado)