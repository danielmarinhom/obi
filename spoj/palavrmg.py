import string
def ordenada(palavra):
  alfabeto = string.ascii_lowercase
  indice = -1
  for letra in palavra:
    atual = alfabeto.index(letra.lower())
    #print(atual, letra)
    if atual < indice:
      return "N"
    elif indice == atual:
      return "N"
    else:
      indice = atual
  return "O"

n = int(input())
palavras = {}
for _ in range(n):
  palavra = input()
  palavras[palavra] = ordenada(palavra)
for k, v in palavras.items():
  print(f'{k}: {v}')