qtd = int(input())
linha = input()
caracteres = []
for caractere in linha:
  caracteres.append(caractere)

def quantidade_caracteres(caracter, caracteres):
  for i, x in enumerate(caracteres):
    if x == caracter:
      intervalo = caracteres[i:]
      return intervalo.count(caracter)


atual = 0
res = ""
for caractere in caracteres:
  if caractere != atual:
    atual = caractere
    res += " " +str(quantidade_caracteres(caractere,caracteres))+ " "+ caractere
print(res.strip())
  