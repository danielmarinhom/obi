n = int(input()) #lances

nomes = []
valores = []

for i in range(n):
  nomes.append(input())
  valores.append(int(input()))

novovalores = sorted(valores, reverse=True)

indice = valores.index(novovalores[0])
print(nomes[indice])
print(novovalores[0])

#10 min