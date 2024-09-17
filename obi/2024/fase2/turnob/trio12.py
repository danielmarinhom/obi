from itertools import combinations

n = int(input())
palitos = list(map(int,input().split()))
def valido(l1, l2, l3):
    return l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2
        

soma = 0
def soma(palitos):
    s = 0
    if len(palitos) < 3:
        return 0
    triangulos = set()
    for i in range(len(palitos)):
        for j in range(len(palitos)):
            for k in range(len(palitos)):
                l1,l2,l3 = palitos[i], palitos[j], palitos[k]
                triangulos.add((l1,l2,l3))
    for l1,l2,l3 in triangulos:
        if valido(l1,l2,l3):
            s+=1
    return s

print(soma(palitos))