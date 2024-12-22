n,b = map(int,input().split())
edges = []
for _ in range(b):
  i,p,j = map(int,input().split())
  edges.append((i-1,p-1,j)) #p - limite

def bellman(edges,n, start):
  cap = [-1]*(n+1)
  cap[start] = float('inf')
  for _ in range(n-1):
    for u,v,w in edges:
      
print(bellman(edges,n,1))