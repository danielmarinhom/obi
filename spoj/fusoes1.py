def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]
def union(a,b):
  rootA = find(a)
  rootB = find(b)
  if rootA != rootB:
    if rootA > rootB:
      parent[rootB] = rootA
    else:
      parent[rootA] = rootB

n,k = map(int,input().split()) # bancos, operacoes
parent = list(range(n+1))
res = []
for _ in range(k):
  linha = input().split()
  a,b = int(linha[1]), int(linha[2])
  if a < 1 or b < 1:
    break
  if linha[0] == 'F':
    union(a,b)
  else:
    if find(a) != find(b):
      res.append("N")
    else:
      res.append("S")
for t in res:
  print(t)
