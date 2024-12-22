a = int(input())
b = int(input())
intervalo = [i for i in range(a,b+1)]

def cubo_quadrado(intervalo):
  n = len(intervalo)
  qtd_quadrado = [False]*n
  qtd_cubo = [False]*n

  cubos = [False]*intervalo[n-1]
  quadrados = [False]*intervalo[n-1]
  total = 0
  for j, numero in enumerate(intervalo):
    for i in range(numero):
      if not quadrados[i] and not cubos[i]:
        quadrados[i] = i**2
        cubos[i] = i**3 
      if quadrados[i] == numero and cubos[i] == numero:
        qtd_quadrado[j] = True

  for i in range(len(qtd_quadrado)):
    if qtd_quadrado[i] and qtd_cubo[i]:
      total += 1
  return total

print(cubo_quadrado(intervalo))