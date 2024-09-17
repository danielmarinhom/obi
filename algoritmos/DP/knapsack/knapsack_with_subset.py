def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)
    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]

def search_subsets(items):
    from itertools import combinations
    for r in range(1, len(items) + 1):
        for subset in combinations(items, r):
            yield subset

# Exemplo de uso
weights = [1, 2, 3]
values = [10, 20, 30]
capacity = 5

max_value = 0
for subset in search_subsets(range(len(weights))):
    subset_weights = [weights[i] for i in subset]
    subset_values = [values[i] for i in subset]
    current_value = knapsack(subset_weights, subset_values, capacity)
    max_value = max(max_value, current_value)

print("Valor máximo:", max_value)