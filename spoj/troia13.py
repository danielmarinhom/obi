n,m = map(int,input().split())  #vertices, entradas
parent = [i for i in range(n)]

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

for _ in range(m):
  a,b = map(int,input().split())
  a,b = a-1, b-1
  union(a,b)

def familias(n):
  fmls = set()
  for x in range(n):
    fmls.add(find(x))
  return len(fmls)
print(familias(n))