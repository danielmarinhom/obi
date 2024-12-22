#soma de cada coluna, soma de cada linha e das duas diagonais sao iguais

linhas = [int(input()) for _ in range(9)]
matriz = [linhas[i:i+3] for i in range(0,9,3)]

soma_linhas = [sum(matriz[i]) for i in range(3)]
soma_colunas = [sum(matriz[i][j] for i in range(3)) for j in range(3)]

soma_diagonal1 = sum(matriz[i][i] for i in range(3)) #a11, a22, a33
soma_diagonal2 = sum(matriz[i][2-i] for i in range(3)) #a13, a22, a31 (0,2), (1,1), (2,0)
#soma da diagonal eh matriz[i][len-1 - i]