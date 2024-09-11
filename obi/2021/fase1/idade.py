#Cibele 1
#Camila 2
#Celeste 3
idades = [0, 0, 0]

for i in range(len(idades)):
  idades[i] = int(input(" > "))

def pega_extremos():
  menor = idades[0]
  maior = menor
  for i in range(len(idades)):
    if(menor >= idades[i]):
      menor = idades[i]
  for i in range(len(idades)):
    if(maior <= idades[i]):
      maior = idades[i]
  return maior, menor

def idade_camila():
  extremos_lista = pega_extremos()
  maior, menor = extremos_lista
  idadesnova = idades
  idadesnova.remove(maior)
  idadesnova.remove(menor)
  return idadesnova


print(idade_camila())