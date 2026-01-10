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

  def find_prefix(self, prefix):
    node = self.root
    for char in prefix:
      if char not in node.children:
        return []
      node = node.children[char]
    words = []
    self._dfs(node, prefix, words)
    return words
  
  def _dfs(self, node, prefix, words):
    if node.endOfWord:
      words.append(prefix)
    for char in sorted(node.children.keys()):
      self._dfs(node.children[char], prefix + char, words)


trie = Trie()
n = int(input())
for _ in range(n):
  trie.insert(input())
m = int(input())
res = []
for _ in range(m):
  res.append(trie.find_prefix(input()))
for t in res:
  print(t)

'''
5
apple
app
application
bat
ball
3
app
ba
ca
'''