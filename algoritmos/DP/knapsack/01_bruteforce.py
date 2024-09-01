from itertools import combinations

def knapsack(values, weights, capacity):
  n = len(values)
  max_profit = 0

  for r in range(n+1):
    for combination in combinations(range(n), r):
      totalW = sum(weights[i] for i in combination)
      totalP = sum(values[i] for i in combination)
      if totalW <= capacity and totalP > max_profit:
        max_profit = totalP
  return max_profit
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
print(knapsack(values, weights, capacity))