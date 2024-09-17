#quantos numeros iguais ou menores a N sao primos para dividir
#lista K de numeros primos que acha que o professor vai usar

n,k = map(int,input().split())
primos = list(map(int,input().split()))

def divisiveis(primos, n):
  numeros = [i for i in range(1,n+1)]
  res = 0
  if len(primos) == 1:
    for primo in primos:
      for numero in numeros:
        if numero % primo != 0:
          res += 1
  else:
    for numero in numeros:
      divisivel = False
      for primo in primos:
        if numero % primo == 0:
          divisivel = True
      if divisivel == False:
        res += 1
  return res
print(divisiveis(primos, n))

#10min