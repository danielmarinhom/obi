n, v = list(map(int,input().split()))
l = list(map(int,input().split()))
def verificar_subset(n, l, v):
  for i in range(n):
    for j in range(n):
      if l[i]+l[j] == v:
        return True
      
print(verificar_subset(n, l, v))