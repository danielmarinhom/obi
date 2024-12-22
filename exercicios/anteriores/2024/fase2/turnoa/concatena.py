n, q = map(int,input().split()) #numero de digitos, quantidade de perguntas
lista = list(map(int,input().split()))
perguntas = []
for _ in range(q):
    st, en = map(int,input().split())
    perguntas.append((st,en))

def potencial(st,en, lista):
    nv = lista[st-1:en]
    soma = 0
    for i in range(len(nv)):
        for j in range(1,len(nv)):
            if j != i:
                x = str(nv[i])+str(nv[j])
                soma += int(x)
            else:
                x = str(nv[i])+str(nv[j-i])
                soma += int(x)
    return soma

for start, end in perguntas:
    print(potencial(start,end, lista))