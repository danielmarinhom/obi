from itertools import permutations
#6 cubos todos de mesmo tamanho mas com pesos possivelmente diferentes (com volumes de areia
#empilhar os cubos para formar uma piramide de 3 andares (3 na base, 2 no meio, 1 em cima)
#os pesos de cada andar devem ser iguais

pesos = []
linha = input().split()
res = "N"
for numero in linha:
  pesos.append(int(numero))

def is_balanced(cubos):
  total = sum(cubos)
  if total % 3 != 0:
    return "N"
  target = total//3
  for perm in permutations(cubos):
    first = perm[0:3]
    second = perm[3:5]
    third = perm[5:6]
    if sum(first) == target and sum(second) == target and sum(third) == target:
      return "S"
  return "N"
print(is_balanced(pesos))