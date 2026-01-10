class TrieNode:
  def __init__(self):
    self.children = {}
    self.endOfWord = False

class Trie:
  def __init__(self):
    self.root = TrieNode() # initializes an empty node as the root

  def insert(self, word):
    node = self.root  # set the current node as the root
    for char in word:
      if char not in node.children: # for each character, check if a child already exists
        node.children[char] = TrieNode() # if it doesn't exist, initialize a node with that child
      node = node.children[char]  # the current node now becomes its child
    node.endOfWord = True # at the end of the characters, mark the current node as the end of a word

  def search(self, word):
    node = self.root
    for char in word:
      if char not in node.children: # if there is no node with child equal to the character
        return False  # return False
      node = node.children[char]  # set the current node as its child
    return node.endOfWord # return True if it reached the end of a word and it is really a word, False otherwise
  
  def starts_with(self, prefix):  
    # iterate through the prefix characters and check if a node with the next character exists
    # if yes, return True; if a node is missing, return False
    node = self.root  
    for char in prefix:
      if char not in node.children:
        return False
      node = node.children[char]
    return True
  
trie = Trie()
trie.insert("hello")
print(trie.search("hello"))  # True
print(trie.search("hell"))   # False
print(trie.starts_with("hell"))  # True
print(trie.starts_with("hello"))  # True
print(trie.starts_with("helloo")) # False
