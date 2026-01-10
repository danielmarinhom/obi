def verificar_matriz_legal(matriz):
    l, c = len(matriz), len(matriz[0])
    for i in range(1, l):
        for j in range(1, c):
            if matriz[0][0] + matriz[i][j] > matriz[0][j] + matriz[i][0]:
                return False
    return True

def maior_submatriz_superlegal(matriz):
    L, C = len(matriz), len(matriz[0])
    maior_area = 0
    
    for l1 in range(L):
        for l2 in range(l1 + 1, L):
            for c1 in range(C):
                for c2 in range(c1 + 1, C):
                    submatriz = [row[c1:c2+1] for row in matriz[l1:l2+1]]
                    if verificar_matriz_legal(submatriz):
                        area = (l2 - l1 + 1) * (c2 - c1 + 1)
                        maior_area = max(maior_area, area)
    
    return maior_area

# Leitura da entrada
tamanhos = input("").split()
l, c = int(tamanhos[0]), int(tamanhos[1])

matriz = []
for i in range(l):
    linha = list(map(int, input("").split()))
    matriz.append(linha)
# Processamento e saída
print(maior_submatriz_superlegal(matriz))
