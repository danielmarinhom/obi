#x bits por y gramas
#24 bits por 250 gramas

#N, numero de supermercados
#P G
#P-preco G-gramas

#saida -> multiplica p*g

n = int(input(""))

precos = []
gramas = []

for i in range(n):
  linha = input("").split()
  precoss, gramass = float(linha[0]), float(linha[1])
  precos.append(precoss)
  gramas.append(gramass)

menor = precos[0]*gramas[0]
menorgrama = 0
for i in range(n):
  if precos[i]*gramas[i] < menor:
    menor = precos[i]
    menorgrama = gramas[i]
paramil = 1000/menorgrama
print(menor*paramil)