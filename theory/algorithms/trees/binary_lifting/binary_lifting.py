def binary_lifting(n, tree):
  log = 20  # maximum number to be considered
  up = [[-1] * log for _ in range(n)] # up[i][j] represents the 2**k-th ancestor of i

  def dfs(node, parent): # node, parent
    up[node][0] = parent  # immediate ancestor 2**0 of node as its parent
    for i in range(1, log): # iterate up to the maximum considered
      if up[node][i-1] != -1:  # if the ancestor at distance 2**(i-1) exists
        up[node][i] = up[ up[node][i-1] ][i-1]  # define the ancestor if it exists

    for child in tree[node]: # run dfs for the children of v
      if child != parent:  # avoid going back to the parent node
        depth[child] = depth[node] + 1  # update depth using parent's depth + 1
        dfs(child,node)

  dfs(0, -1) # assume the root is 0, -1 because the root has no parent
  return up

def lca(u,v,up):
  log = len(up[0])
  if depth[u] < depth[v]: # if depth of u < v, swap to ensure u is deeper
    u, v = v, u
  diff = depth[u] - depth[v]  # difference between depths of u and v
  for i in range(log):  # move u up until both are at the same depth
    if (diff >> i) & 1:
      u = up[u][i]
  if u == v:  # if they are the same, return one of them
    return u
  for i in range(log-1, -1, -1):  
    # move u and v up at the same time to find the closest common ancestor
    if up[u][i] != up[v][i]:
      u = up[u][i]
      v = up[v][i]
  return up[u][0] # the common ancestor is the parent of the current u and v nodes

# the tree structure is a dictionary of lists
tree = {0: [1, 2], 1: [0, 3, 4], 2: [0, 5, 6], 3: [1], 4: [1], 5: [2], 6: [2]}
n = len(tree)
depth = [0]*n

def calculate_depth(v, p, d): # v - current node, p - parent of v, d - current depth
  depth[v] = d
  for u in tree[v]:
    if u != p:
      calculate_depth(u, v, d+1)

calculate_depth(0,-1,0)

up = binary_lifting(n,tree)
print(lca(4,5,up))
