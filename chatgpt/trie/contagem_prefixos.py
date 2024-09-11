class TrieNode:
  def __init__(self) -> None:
    self.children = {}
    self.endOfWord = False
    self.prefix_count = 0
class Trie:
  def __init__(self) -> None:
    self.root = TrieNode()
  def insert(self, string):
    node = self.root
    for char in string:
      if char not in node.children:
        node.children[char] = TrieNode()
      node = node.children[char]
      node.prefix_count += 1
    node.endOfWord = True
  def count_prefix(self, prefix):
    node = self.root
    for char in prefix:
      if char not in node.children:
        return 0
      node = node.children[char]
    return node.prefix_count

trie = Trie()
n = int(input())
for _ in range(n):
  trie.insert(input())
q = int(input())
res = []
for _ in range(q):
  res.append(trie.count_prefix(input()))
for t in res:
  print(t)