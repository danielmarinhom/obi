from itertools import combinations

n = int(input())
palitos = list(map(int,input().split()))
def valido(l1, l2, l3):
    return l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2
        

def soma(palitos):
    s = 0
    if len(palitos) < 3:
        return 0
    for perm in combinations(palitos, r=3):
        l1,l2,l3 = perm
        if valido(l1,l2,l3):
            s += 1
    return s

print(soma(palitos))