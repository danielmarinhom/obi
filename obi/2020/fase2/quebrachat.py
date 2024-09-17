def max_valor_configuracao(colunas, linhaUm, linhaDois):
    max_valor = float('-inf')

    for i in range(colunas):
        soma = sum(linhaUm[j] * linhaDois[(j + i) % len(linhaDois)] for j in range(colunas))
        if soma > max_valor:
            max_valor = soma
    
    return max_valor

# Entrada de dados
colunas = int(input(" > "))
linhaUm = list(map(int, input(" > ").split()))
linhaDois = list(map(int, input(" > ").split()))

print(max_valor_configuracao(colunas, linhaUm, linhaDois))
