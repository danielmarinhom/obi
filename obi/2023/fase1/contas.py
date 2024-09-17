v = int(input()) #dinheiro na conta do veio
a = int(input()) #acougue
f = int(input()) #farmacia
p = int(input()) #padaria

contas = [a,f,p]
contas.sort()
contador = 0
for conta in contas:
  if v >= conta:
    v -= conta
    contador += 1
print(contador)

#2min 44s