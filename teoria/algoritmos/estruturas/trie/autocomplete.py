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
    node = self.root()
    for char in string:
      if char not in node.children:
        return False
      node = node.children[char]
    return node
  def words_with_prefix(self, prefix):
    def dfs(node, prefix):
      if node.endOfWord:
        results.append(prefix)
      for char in sorted(node.children.keys()):
        dfs(node.children[char], prefix+char)
    results = []
    node = self.search(prefix)
    if node:
      dfs(node, prefix)
    return results