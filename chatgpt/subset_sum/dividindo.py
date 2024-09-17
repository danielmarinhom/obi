n = int(input())
valores = list(map(int,input().split()))
target = int(input())

def subset(valores, target):
  dp = [False]*(target+1)
  dp[0] = True
  for valor in valores:
    for i in range(target, valor-1, -1):
      if dp[i-valor]:
        dp[i] = True
  return "SIM" if dp[target] else "NAO"

print(subset(valores,target))