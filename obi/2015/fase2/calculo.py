#o primeiro digito binario representa 2**-1, o segundo 2**-2, o terceiro 2**-3
#0 1 -> 0*2-1 + 1*2-2 = 0.25
#1 0 1 0 1 1 -> 1*2-1 + 0*2-2 + 1*2-3 + 0*2-4 + 1*2-5 + 1*2-6 = 0.671875

#M, N - numero de digitos binarios de X e de Y
#M numeros X_i
#N numveros Y_i

#X+Y

m, n = list(map(int, input().split()))

x = list(map(int, input().split()))
y = list(map(int, input().split()))

def calcular_binario(x, n):
  res = 0
  for i in range(n):
    res += x[i]*2**-(i+1)
  return res

def recalcular_binario(valor):
  binarios = []
  pot = 1
  while valor > 0:
    if valor >= 2**-pot:
      binarios.append(1)
      valor -= 2**-pot
    else:
      binarios.append(0)
    pot+=1
  return binarios
j = calcular_binario(y,n) + calcular_binario(x,m)
l = "".join(map(str,recalcular_binario(j)))
for letra in l:
  print(l)