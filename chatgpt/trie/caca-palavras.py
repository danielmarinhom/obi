'''
Dada uma matriz de caracteres e uma lista de palavras, encontre todas as palavras
da lista que estão presentes na matriz. As palavras podem ser formadas por letras 
adjacentes horizontalmente ou verticalmente.

Entrada:

Um inteiro n representando o número de palavras na lista.
n linhas seguintes, cada uma contendo uma palavra.
Dois inteiros m e p representando as dimensões da matriz.
m linhas seguintes, cada uma contendo p caracteres separados por espaços.
Saída:

Todas as palavras encontradas na matriz, uma por linha, em ordem lexicográfica.
Se nenhuma palavra for encontrada, imprima "Nenhuma palavra encontrada".
'''
class TrieNode:
  def __init__(self) -> None:
    self.children = {}
    self.endOfWord = False
class Trie:
  def __init__(self) -> None:
    self.root = TrieNode()
  def insert(self, string):
    node = self.root
    for char in string:
      if char not in node.children:
        node.children[char] = TrieNode()
      node = node.children[char]
    node.endOfWord = True
  
def dfs(matriz, node, x, y, visited, results, path):
  if node.endOfWord:
    results.add(path)
  directions = [(0,-1),(0,1),(1,0),(-1,0)] #norte, sul, leste, oeste 
  for dx, dy in directions:
    nx, ny = x+dx, y+dy
    if 0 <= nx < len(matriz) and 0 <= ny < len(matriz[0]) and not visited[nx][ny]:
      char = matriz[nx][ny]
      if char in node.children:
        visited[nx][ny] = True
        dfs(matriz, node.children[char], nx, ny, visited, results, path + char)
        visited[nx][ny] = False

trie = Trie()
n = int(input()) #palavras
for _ in range(n):
  trie.insert(input())
m, p = map(int,input().split()) #linhas, colunas
matriz = []
for _ in range(m):
  matriz.append(input().split())

visited = [[False]*p for _ in range(m)]
results = set()
for i in range(m):
  for j in range(p):
    char = matriz[i][j]
    if char in trie.root.children:
      visited[i][j] = True
      dfs(matriz, trie.root.children[char], i, j, visited, results, char)
      visited[i][j] = False

if results:
  for i in sorted(results):
    print(i)
else:
  print("Nenhuma palavra encontrada")