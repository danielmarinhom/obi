#1 - 1 por 1
#2 - metade de 1
#3 - metade de 2

#4 do tipo 3 para os cantos

largura = int(input("Largura > "))
altura = int(input("Altura > "))

lajotas = {1: [], 2: [], 3: []}

area = largura * altura
lajotas[1].append(area)
lajotas[2].append(1)
lajotas[1] = sum(lajotas[1])
print(lajotas[1])


