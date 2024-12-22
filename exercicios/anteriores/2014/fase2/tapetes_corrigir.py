#se n = 4 e dimensoes = [(2,2),(4,4),(6,6),(3,3)], comprimento = 2+4+6+3
#

l,n = map(int,input().split()) #l - comprimento do tubo, n - quantidade de tapetes

def max_sum(l,n):
  tapetes = []
  for size in range(l,0,-1):
    while size <= l and n > 0:
      tapetes.append(size)
      l-=size
      n-=1
  if n == 0 and l == 0:
    total = sum([x*x for x in tapetes])
    return total
  else:
    return -1
print(max_sum(l,n))