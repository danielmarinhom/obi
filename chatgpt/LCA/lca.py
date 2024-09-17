n, q = map(int,input().split())
edges = []
for _ in range(n-1):
  u,v = map(int,input().split())
  edges.append((u,v))
nos = []
for _ in range(q):
  a, b = map(int,input().split())
  nos.append((a,b))

def binary_lifting(n, tree):
