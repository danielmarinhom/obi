from itertools import permutations
import math
#concatenados = set()
n, q = map(int,input().split()) #numero de digitos, quantidade de perguntas
lista = list(map(int,input().split()))
perguntas = []
for _ in range(q):
    st, en = map(int,input().split())
    perguntas.append((st,en))

def potencial(st,en, lista):
    nv = lista[st-1:en]
    soma = 0
    perm = []
    for i in range(len(nv)):
        for j in range(1,len(nv)):
            if j != i:
                perm.append(str(nv[i])+str(nv[j]))
            else:
                perm.append(str(nv[i])+str(nv[j-i]))
    for num in perm:
        soma += int(num)
    return soma
res = []
for start, end in perguntas:
    res.append(potencial(start,end, lista))
for x in res:
    print(x)