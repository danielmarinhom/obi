from itertools import permutations, combinations
n = int(input())
palitos = list(map(int,input().strip().split()))


def valido(l1, l2, l3):
    return l1 + l2 > l3 and l2 + l3 > l1



triangulos = set()
soma = 1

#permutations
for perm in combinations(palitos, r=3):
    l1,l2,l3 = perm
    if ((l1,l2,l3) not in triangulos and
        (l1,l3,l2) not in triangulos and

        (l2,l1,l3) not in triangulos and
        (l2,l3,l1) not in triangulos and

        (l3,l1,l2) not in triangulos and
        (l3,l2,l1) not in triangulos 
        
        ):
        triangulos.add(perm)
#testes
for l1, l2, l3 in triangulos:
    if valido(l1,l2,l3):
        soma += 1
        print(l1,l2,l3)
print(soma)