def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)] #os +1 eh para o caso de 0 itens

    for i in range(1, n + 1): #comecamos de 1 porque i = 0 eh a base do problema
        for w in range(capacity + 1): #queremos considerar todas as capacidades possiveis
            if weights[i - 1] <= w: #tem que estar dentro da capacidade
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]) #valor maximo que podemos obter com o item atual
            else:   
                dp[i][w] = dp[i - 1][w] #valor maximo que podemos obter sem o item atual
    
    return dp[n][capacity] #retorna o valor maximo considerando todos os n itens e a capacidade total da mochila


#KNAPSACK DO EXEMPLO DO TXT:
def knapsack(capacity, items):
    # Inicializa a tabela DP com 0s
    dp = [0] * (capacity + 1)
    
    # Preenche a tabela DP
    for weight, value in items:
        for w in range(capacity, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)
    
    return dp[capacity]