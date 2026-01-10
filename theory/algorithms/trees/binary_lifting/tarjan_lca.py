def find(x, parent):
  if parent[x] != x:
    parent[x] = find(parent[x], parent)
  return parent[x]
def union(a,b, parent):
  rootA = find(a)
  rootB = find(b)
  if rootA != rootB:
    if rootA > rootB:
      parent[rootB] = rootA
    else:
      parent[rootA] = rootB

def tarjan_lca(n, edges, queries):
  tree = [[] for _ in range(n)]
  for u,v in edges:
    tree[u].append(v)
    tree[v].append(u)
  parent = list(range(n))
  ancestor = list(range(n))
  visited = [False] * n
  lca_result = {}
  
  query_list = [[] for _ in range(n)]
  for a, b in queries:
    query_list[a].append(b)
    query_list[b].append(a)
  
  def dfs(u):
    visited[u] = True
    for v in tree[u]:
      if not visited[v]:
        dfs(v)
        union(u,v, parent)
        ancestor[find(u, parent)] = u
    for v in query_list[u]:
      if visited[v]:
        lca = ancestor[find(v, parent)]
        if visited[v]:
          lca = ancestor[find(v, parent)]
          lca_result[(u,v)] = lca
          lca_result[(v,u)] = lca
  dfs(0)
  return lca_result
