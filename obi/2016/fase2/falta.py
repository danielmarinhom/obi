from itertools import permutations


n = int(input())
resultado = 1
contador = 1
while contador <= n:
  resultado *= contador
  contador += 1

diferentes = []
for _ in range(resultado-1):
  diferentes.append(tuple(map(int,input().split())))

def restante(diferentes,n):
  permutacoes = []
  tipos = [i for i in range(1,n+1)]
  for perm in permutations(tipos):
    permutacoes.append(perm)
  for l in diferentes:
    if l in permutacoes:
      permutacoes.remove(l)
  return permutacoes[0]

res = restante(diferentes,n)
final = ""
for numero in res:
  final += str(numero) + " "
print(final)

#25 min