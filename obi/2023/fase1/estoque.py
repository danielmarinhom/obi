#m,n - numero de tipos, numero de tamanhos no estoque
#m linhas seguintes contem n inteiros xij indicando a quantidade de roupas do tipo i e tamanho j
#inteiro p - com o numero de pedidos
#p linhas seguintes contem i e j- tipo e tamanho da peca

m, n = map(int,input().split())
roupas = [[]*m for _ in range(n)]
for _ in range(m):
  quantidade, tipo, tamanho = map(int,input().split())
  roupas[tipo-1][tamanho-1] = quantidade

p = int(input())
pedidos = []

for _ in range(p):
  i,j = map(int,input().split())
  pedidos.append((i-1,j-1))

def verificar_disponibilidade(pedidos, roupas):
  res = 0
  for i,j in pedidos:
    if roupas[i][j] > 0:
      res += 1

  return res

print(verificar_disponibilidade(pedidos, roupas))