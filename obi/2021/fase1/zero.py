numeros = []

qtd_numeros = int(input(" > "))
print("--------")

for _ in range (qtd_numeros):
  numero = int(input(" > "))
  if(numero != 0):
    numeros.append(numero)
  else:
    numeros.pop()

soma = sum(numeros)

print("--------")
print(numeros)
print(soma)