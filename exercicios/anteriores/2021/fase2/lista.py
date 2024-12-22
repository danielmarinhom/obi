#L[i] = L[N-i+1]
#dois elementos adjacentes substitua por um unico elemento de valor igual a soma dos antigos
#quando contrai os elementos deccresce um elemento
#


def palindromo(numeros, n):
  res = 0
  for i in range(n):
    if i > 0 and numeros[i] == numeros[n-i]:
      return True
    
def contracao(numeros, n):
  res = 0
  while not palindromo(numeros, n):
    for i in range(n):
      #dois elementos adjacentes = um elementos com valor igual a soma dos elementos substituidos
      if i < n:
        elemento = numeros[i]+numeros[i+1]
        numeros.replace(numeros[i], elemento)
        numeros.pop(numeros[i+1])
      else:
        elemento = numeros[i]+numeros[i-1]
        numeros.replace(numeros[i], elemento)
        numeros.pop(numeros[i-1])
      res += 1
  return res

N = int(input(""))
l = input("").strip().split()
numeros = l

print(contracao(numeros, N))