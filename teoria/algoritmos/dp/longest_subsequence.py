def longest_palindromic_subsequence(s):
    n = len(s)
    # Cria uma tabela dp de tamanho n x n
    dp = [[0] * n for _ in range(n)]

    # Cada caractere é um palíndromo de comprimento 1
    for i in range(n):
        dp[i][i] = 1

    # Preenche a tabela dp
    for length in range(2, n + 1):  # comprimento das substrings
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # A resposta está na posição dp[0][n-1]
    return dp[0][n - 1]

# Exemplo de uso
s = "BBABCBCAB"
print(longest_palindromic_subsequence(s))  # Saída: 7
