n = int(input())
pesos = []
for _ in range(n):
  pesos.append(int(input()))

def caravana(pesos,n):
  media = sum(pesos) // n
  resultado = []
  for peso in pesos:
    resultado.append(media-peso)
  return resultado
resultado = caravana(pesos,n)
for result in resultado:
  print(result)