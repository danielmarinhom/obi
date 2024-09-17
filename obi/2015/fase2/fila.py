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
    res += i*2**-(i+1)
  return res
print(calcular_binario(x,m) + calcular_binario(y,n))

