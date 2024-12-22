n,w = map(int,input().split())
itens = []
for _ in range(n):
  weight, value = map(int,input().split())
  itens.append((weight,value))
print(itens)
def knapsack(itens,maximo,n):
  dp = [[0 for _ in range(maximo+1)] for _ in range(n+1)]
  for i in range(1,n+1):
    weight,value = itens[i-1]
    for w in range(maximo+1):  
      if weight <= w:
        dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)
      else:
        dp[i][w] = dp[i-1][w]
  return dp[n][maximo]
print(knapsack(itens,w,n))