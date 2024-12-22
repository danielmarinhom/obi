from itertools import combinations
n = int(input())
palitos = list(map(int,input().strip().split()))

#def valido(l1, l2, l3):
#    return l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2

soma = 0

#permutations
for perm in combinations(palitos, r=3):
    l1,l2,l3 = perm
    if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
        soma += 1
"""
#testes
for l1, l2, l3 in triangulos:
    if valido(l1,l2,l3):
        soma += 1
        #print(l1,l2,l3)
"""
print(soma)