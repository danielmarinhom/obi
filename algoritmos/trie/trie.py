class TrieNode:
  def __init__(self):
    self.children = {}
    self.endOfWord = False
class Trie:
  def __init__(self):
    self.root = TrieNode() # inicia o node vazio como raiz
  def insert(self, word):
    node = self.root  # define o nodo atual como a raiz
    for char in word:
      if char not in node.children: # para cada caractere ele verifica se ja existe um filho igual
        node.children[char] = TrieNode() # se nao existir ele inicializa um node com aquele filho
      node = node.children[char]  # o node atual passa a valer o filho dele
    node.endOfWord = True # no final dos caracteres define o node atual como o fim de uma palavra

  def search(self, word):
    node = self.root
    for char in word:
      if char not in node.children: # se nao existir um node com filho = ao caractere
        return False  # retorna False
      node = node.children[char]  # define o node atual como o filho dele
    return node.endOfWord # retorna True se chegou ao fim da palavra e ela eh realmente uma palavra e False se nao
  
  def starts_with(self, prefix):  
    # roda os caracteres do prefixo e verifica se existe um nodo com o proximo caractere
    # se sim, retorna True, se faltar um nodo do proximo caractere, False
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