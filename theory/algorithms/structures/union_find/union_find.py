#verifica a conexao de elementos em um grafo separando eles por parentesco

def initialize(size):
    global parent, rank
    parent = [i for i in range(size)]
#nessa parte ele verifica se o pai do elemento x eh igual a ele mesmo (logo ele eh o pai do grupo)
#se o pai do grupo nao for ele, ele chama recursivamente o pai desse numero (que nao eh ele)
def find(x):  #p -> parent
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]

def union(p,q):
  rootP = find(p)   #encontra o representante do grupo P
  rootQ = find(q)   #encontra o representante do grupo Q

  if rootP != rootQ:  #verifica se os representantes sao diferentes
    if rootP > rootQ:
      parent[rootQ] = rootP
    else:
      parent[rootP] = rootQ

def connected(p, q):
  return find(p) == find(q)


union(0, 1)
union(1, 2)
print(connected(0,2))
print(connected(0,3))



#EXEMPLO
#verifica se as cidades estao conectadas por estradas e verifica se todas tem o mesmo representante
n=5
estradas = [(0,1), (1,2), (3,4)]
def todas_conectadas(n,estradas):
  initialize(n)
  for u, v in estradas:
    union(u,v)
  primeiro_representante = find(0)
  for i in range(1,n):
    if find(i) != primeiro_representante:
      return False
  return True

n = 5
estradas = [(0, 1), (1, 2), (3, 4)]
print(todas_conectadas(n, estradas))  # False, pois 3 e 4 não estão conectados a 0, 1, e 2

estradas = [(0, 1), (1, 2), (2, 3), (3, 4)]
print(todas_conectadas(n, estradas))  # True, pois todas as cidades estão conectadas