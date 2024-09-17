#algum lado possua um buraco
#nem que cada pedaco de um palitinho exceda o limite do triangulo

# a soma de qualquer dois lados é maior que o tamaanho do terceiro lado

n = int(input())
palitos = list(map(int,input().strip().split()))

#print(palitos)

def valido(l1, l2, l3):
    return l1 + l2 > l3 and l2 + l3 > l1

soma = 0

usados = set()
for i in range(2,len(palitos)):

    l1, l2, l3 = palitos[i], palitos[i-1], palitos[i-2]
    #print(l1,l2,l3)
    if valido(l1,l2,l3) and (l1,l2,l3) not in usados:
        usados.add((l1,l2,l3))
        soma += 1

#print(usados)
print(soma)

