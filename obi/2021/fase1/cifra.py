import string

alfabeto = string.ascii_lowercase
vogais = 'aeiou'
palavra = input(" > ")
novapalavra = []

def cifrar_palavra():
  for letra in palavra:
    if letra in vogais:
      novapalavra.append(letra)
    else:
      novapalavra.append(letra+procurar_vogal(letra)+procurar_consoante(letra))
  return "".join(novapalavra)

def procurar_vogal(consoante:str):
  menor_distancia = float('inf')
  vogal_proxima = ''
  for vogal in vogais:
    distancia = abs(alfabeto.index(consoante)- alfabeto.index(vogal))
    if distancia < menor_distancia:
      menor_distancia = distancia
      vogal_proxima = vogal
    elif distancia == menor_distancia:
      if alfabeto.index(vogal) < alfabeto.index(vogal_proxima):
        vogal_proxima = vogal
  return vogal_proxima
  
def procurar_consoante(consoante:str):
  indice = alfabeto.index(consoante)+1
  while indice < len(alfabeto):
    if alfabeto[indice] not in vogais:
      return alfabeto[indice]
    indice += 1
  return consoante


print(cifrar_palavra())
