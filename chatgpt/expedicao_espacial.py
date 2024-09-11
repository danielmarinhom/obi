n,m,f = map(int,input().split()) #n - num planetas, m - num portais, f - combustivel maximo
portais = []
for _ in range(m):
  u,v,w = map(int,input().split())
  portais.append((u,v,w))
s = int(input())  #start
d = int(input())  #end
#------------------------
def bfs(portais, start,end, maximo):
  queue = [(start,0)]
  visited = set([start])
  while queue:
    atual, combustivel = queue.pop(0)
    if atual == end:
      return combustivel
    for u,v,w in portais:
      if atual == u and combustivel+w <= maximo:
        queue.append((v,combustivel+w))
        visited.add(v)
      if atual == v and combustivel+w <= maximo:
        queue.append((u,combustivel+w))
        visited.add(u)
  return "IMPOSSIVEL"
print(bfs(portais,s,d,f))
      
