#duas linhas, n colunas
colunas = int(input(" > "))
linhaUm = input(" > ")
linhaDois = input(" > ")

listaUm = list(map(int, linhaUm.strip().split()))
listaDois = list(map(int, linhaDois.strip().split()))

def somas():
  soma = []
  #primeira soma
  for i, numeros in enumerate(listaUm):
   soma.append((numeros*int(listaDois[i])))
  #soma trocando
  if verifica_menor(listaDois):
    novalista = transforma_lista(listaUm)
    for i, numeros in enumerate(novalista):
      if i < len(listaDois):
        soma.append((numeros*int(listaDois[i])))
  if verifica_menor(listaUm):
    novalista = transforma_lista(listaDois)
    for i, numeros in enumerate(novalista):
      if i < len(listaUm):
        soma.append((numeros*int(listaUm[i])))
  
  return soma

def verifica_menor(lista: list):
  return len(lista) < colunas

def transforma_lista(lista1:list):
  novalista = [0] * (colunas - len(lista1)) + lista1
  return novalista


print(somas())