def binary_lifting(n, tree):
  log = 20  # numero maximo a ser considerado
  up = [[-1] * log for _ in range(n)] # up[i][j] representa o 2**k-esimo ancestral de i

  def dfs(node, parent): # nodo, pai
    up[node][0] = parent  # ancestral imediato de 2**0 de nodo como pai dele
    for i in range(1, log): # roda o maximo a ser considerado
      if up[node][i-1] != -1:  # se o ancestral na distancia 2**(i-1) existe
        up[node][i] = up[ up[node][i-1] ][i-1]  # define o ancestral caso exista

    for child in tree[node]: # executamos o dfs para os filhos de v
      if child != parent:  # evitamos voltar ao nodo pai
        depth[child] = depth[node] + 1  #atualiza a profundidade usando o pai do nodo + 1
        dfs(child,node)

  dfs(0, -1) # assume que a raiz eh 0, -1 eh pq a raiz nao tem pai
  return up

def lca(u,v,up):
  log = len(up[0])
  if depth[u] < depth[v]: # se a profundidade de u < v, trocamos para garantir que u eh mais profundo
    u, v = v, u
  diff = depth[u] - depth[v]  # diferenca entre a profundidade de u e v
  for i in range(log):  # movemos u para cima ate que ambos estejam na mesma profundidade
    if (diff >> i) & 1:
      u = up[u][i]
  if u == v:  # se eles sao o mesmo nos retornamos um deles
    return u
  for i in range(log-1, -1, -1):  
    # movemos u e v para cima ao mesmo tempo para encontrar o ancestral comum mais proximo
    if up[u][i] != up[v][i]:
      u = up[u][i]
      v = up[v][i]
  return up[u][0] # o ancestral comum eh o pai dos nos u e v atuais

# a estrutura da arvore eh um dicionario de listas
tree = {0: [1, 2], 1: [0, 3, 4], 2: [0, 5, 6], 3: [1], 4: [1], 5: [2], 6: [2]}
n = len(tree)
depth = [0]*n

def calculate_depth(v, p, d): # v - no atual, p - pai de v, d - profundidade atual
  depth[v] = d
  for u in tree[v]:
    if u != p:
      calculate_depth(u, v, d+1)

calculate_depth(0,-1,0)

up = binary_lifting(n,tree)
print(lca(4,5,up))
