data = input().split()
N = int(data[0])
M = int(data[1])
relacoes = [(int(data[i]), int(data[i+1])) for i in range(2, len(data), 2)]


def dfs(n):
  graph = [[] for _ in range(n+1)]
  stack = 

   #(Tree Decomposition) ou Tabela Esparsa,
   #segment tree, fenwick tree
   #merge sort tree
   #trie
   #tarjan para pontes e pontso de articulacao