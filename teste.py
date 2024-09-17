#DFS
#KRUSKAL

def prefixo(array, index):
  return sum(array[:index+1])
def atualizacao(array, index, valor):
  array[index] = valor
  return array
n,q = map(int,input().split())
elementos = list(map(int,input().split()))
op = []
results = []
for _ in range(q):
  x = input().split()
  if x[0] == '1':
    results.append(prefixo(elementos, int(x[1])))
  else:
    elementos = atualizacao(elementos,int(x[1])-1, int(x[2]))
for resp in results:
  print(resp)