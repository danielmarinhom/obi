linhas = [int(input()) for _ in range(9)]

matriz = [linhas[i:i+3] for i in range(0, 9, 3)]
 
maior_valor = max(linhas)

for i in range(3):
    for j in range(3):
        if matriz[i][j] == maior_valor:
            matriz[i][j] = -1

for linha in matriz:
    print(' '.join(map(str, linha)))