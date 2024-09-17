qtd = int(input())
linha = input()

def rle_compressao(cadeia):
    if not cadeia:
        return ""
    
    n = len(cadeia)
    resultado = []
    i = 0
    
    while i < n:
        contagem = 1
        while i + 1 < n and cadeia[i] == cadeia[i + 1]:
            i += 1
            contagem += 1
        resultado.append(f"{contagem} {cadeia[i]}")
        i += 1
    
    return " ".join(resultado)

print(rle_compressao(linha))
