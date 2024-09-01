def rod_cutting(price, n):
    dp = [0] * (n + 1)

    # Itera sobre cada tamanho de haste de 1 até n
    for i in range(1, n + 1):
        max_val = -1
        # Para cada tamanho de haste 'i', tenta cortar em tamanhos 'j' e 'i-j-1'
        for j in range(i):
            max_val = max(max_val, price[j] + dp[i - j - 1])
        dp[i] = max_val

    return dp[n]
price = [1, 5, 8, 9]

