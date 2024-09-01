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
def dfs(matriz, node, x, y, path, visited, results):
  if node.endOfWord:
    results.add(path)
  directions = [(0,-1),(0,1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)] #norte sul leste oeste
  for dx, dy in directions:
    nx, ny = x+dx, y+dy
    if 0 <= nx < len(matriz) and 0 <= ny < len(matriz[0]) and not visited[nx][ny]:
      char = matriz[nx][ny]
      if char in node.children:
        visited[nx][ny] = True
        dfs(matriz, node.children[char], nx, ny, path+char, visited, results)
        visited[nx][ny] = False

trie = Trie()
n = int(input())
for _ in range(n):
  trie.insert(input())
x,y = map(int,input().split())
matriz = []
for _ in range(x):
  matriz.append(input().split())

results = set()
visited = [[False]*y for _ in range(x)]
for i in range(x):
  for j in range(y):
    char = matriz[i][j]
    if char in trie.root.children:
      visited[i][j] = True
      dfs(matriz, trie.root.children[char], i, j, char, visited, results)
      visited[i][j] = False
for y in sorted(results):
  print(y)
'''
8
word
diagonal
vertical
horizontal
maze
search
found
sex
12 12
R E I H A R T L W O R D
T T T D E R N S T W M N
H A V U O N L P S D R S
P O E L I P S D I A G V
W B R E I H L A R E E C
O H T I F T G S A N R W
G A I T Z O S G O O M U
L D C M N O U O S H I C
H E A A Y R N N D L A I
A E L Z C L S T D I E E
A D U E E L S E A R C H
C M L A E P Y A O L D U
'''