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
  def search(self,string):
    node = self.root
    for char in string:
      if char not in node.children:
        return False
      node = node.children[char]
    return "Sim" if node.endOfWord else "Nao"
  def find_prefix(self,string):
    node = self.root
    for char in string:
      if char not in node.children:
        return False
      node = node.children[char]
    return True

trie = Trie()

n = int(input())

resp = []
for _ in range(n):
  query = input().split()
  if query[0] == 'insert':
    trie.insert(query[1])
  elif query[0] == 'search':
    resp.append(trie.search(query[1]))
  elif query[0] == 'starts_with':
    x = trie.find_prefix(query[1])
    resp.append("Sim" if x else "Nao")

for res in resp:
  print(res)