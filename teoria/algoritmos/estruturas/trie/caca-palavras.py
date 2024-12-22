class TrieNode:
  def __init__(self):
    self.children = {}
    self.endOfWord = False
class Trie:
  def __init__(self):
    self.root = TrieNode()
  def insert(self, string):
    node = self.root
    for char in string:
      if char not in node.children:
        node.children[char] = TrieNode()
      node = node.children[char]
    node.endOfWord = True
  def search(self, string):
    node = self.root
    for char in string:
      if char not in node.children:
        return False
      node = node.children[char]
    return node
  
def dfs(matriz, node, i, j, path, visited, results):
  if node.endOfWord:
    results.add(path)
  directions = [(0,-1),(0,1),(1,0),(-1,0)] #norte sul leste oeste
  for di, dj in directions:
    ni, nj = i+di, j+dj
    if 0 <= ni < len(matriz) and 0 <= nj < len(matriz[0]) and not visited[ni][nj]:
      char = matriz[ni][nj]
      if char in node.childresn:
        visited[ni][nj] = True
        dfs(matriz,node.children[char], ni, nj, path + char, visited, results)
        visited[ni][nj] = False

trie = Trie()
n = int(input()) # palavras no dicionario
for _ in range(n):
  palavra = input()
  trie.insert(palavra)

m,p = map(int,input().split()) # linhas e colunas
matriz = []
for _ in range(m):
  linha = input().split()
  matriz.append(linha)
#palavras sao horizontais e verticais
results = set()
visited = [[False for _ in range(p)] for _ in range(m)]
for i in range(m):
  for j in range(p):
    char = matriz[i][j]
    if char in trie.root.children:
      visited[i][j] = True
      dfs(matriz, trie.root.children[char], i, j, char, visited, results)
      visited[i][j] = False
if results:
  for word in sorted(results):
    print(word)
else:
  print("Nenhuma palavra encontrada")

'''
5
hello
hell
he
heaven
heavy
4 5
h e l l o
e v a e n
a h e a v
v e n a h
'''



