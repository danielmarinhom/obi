n,w = map(int,input().split())
valor, peso = [], []
for _ in range(n):
  vi,wi = map(int,input().split())
  valor.append(vi)
  peso.append(wi)

def knapsack(pesos, valores, capacidade):
  n = len(pesos)
  dp = [[0]*(capacidade+1) for _ in range(n)]
  print(dp)

print(knapsack(peso, valor, w))