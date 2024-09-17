#3 int (S, A, B)
#quantos numeros do intervalo A, B tem a soma de seus digitos igual a S
#
s, a, b = int(input("")), int(input("")), int(input(""))
intervalo = [i for i in range(a,b+1)]
def iguais(intervalo, s):
  res = 0
  for numero in intervalo:
    soma = 0
    for digito in str(numero):
      soma += int(digito)
    if soma == s:
      res += 1
  return res
print(iguais(intervalo,s))
#3 e 30