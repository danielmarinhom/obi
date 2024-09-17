#N nos e N-1 arestas
n = int(input())
def binary_lifting(n, edges, queries):
  log = 20
  tree = [[] for _ in range(n)]
  up = [[-1] * log for _ in range(n)]
  global depth 
  depth = [0]*n

  for u,v in edges:
    tree[u-1].append(v-1)
    tree[v-1].append(u-1)
  
  def dfs(v, p):
    up[v][0] = p
    for i in range(1, log):
      if up[v][i-1] != -1:
        up[v][i] = up[ up[v][i-1] ][i-1]
    for children in tree[v]:
      if children != p:
        dfs(children,v)
  dfs(0, -1)
  return up
def lca(up, v, u):
  log = len(up[0])
  if depth[u] < depth[v]:
    u,v = v,u
  diff = depth[u] - depth[v]
  for i in range(log):
    if (diff >> i) & 1:
      u = up[u][i]
  if u == v:
    return u
  for i in range(log-1, -1, -1):
    if up[u][i] != up[v][i]:
      u = up[u][i]
      v = up[v][i]
  return up[u][0]