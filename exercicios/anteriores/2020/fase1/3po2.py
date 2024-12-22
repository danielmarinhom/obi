#paga pelos 2 mais caros
#se levar mais que 3, agrupa em 3 e leva o mais barato de cada grupo gratuitamente
#N, numero de chocolates
#P, preco dos chocolates

n = int(input(" > "))
p = []
grupos = []

for numero in range(n):
  x = int(input(" > "))
  p.append(x)

p.sort()
def retirar_menor(lista:list):
  if len(lista) == 1:
    return lista[0]
  lista.pop(0)
  return sum(lista)
  

soma = 0
for i in range(len(p), 0, -3):
  x = p[i-3:i]
  if x != []:
    soma += retirar_menor(x)
  elif len(p) % 3 == 1:
    soma += p[0]
  elif len(p) % 3 == 2:
    soma += p[0] + p[1]
print("soma FINAL > ",soma)
