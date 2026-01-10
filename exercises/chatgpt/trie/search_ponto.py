import time
start = time.time()
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.endOfWord = True

    def search(self, word):
        def dfs(node, index):
            if index == len(word):
                return node.endOfWord
            char = word[index]
            if char == '.':
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
            elif char in node.children:
                return dfs(node.children[char], index + 1)
            return False
        return dfs(self.root, 0)

palavras = [
    "supercalifragilisticexpialidociou",
    "pseudopseudohypoparathyroidis",
    "floccinaucinihilipilificatio",
    "antidisestablishmentarianis",
    "honorificabilitudinitatibu",
    "thyroparathyroidectomizedd",
    "dichlorodifluoromethanee",
    "incomprehensibilitiessss",
    "psychoneuroendocrinologica",
    "hepaticocholangiocholecystentero"
]

# Consultas longas ajustadas
querys = [
    "supercali......isticexpialidociou",
    "pseudop.....hypoparathyroidis",
    "floccinaucini...ipllificatio",
    "anti...establis.mentarianis",
    "hono..ficab..itudi..tatibu",
    "thyrop......roidectomizedd",
    "dichlorodi......methanee",
    "incom.rehensibilitie....",
    "psycho.euroendocrino......",
    "hepa.icocholang.ochole..stentero"
]

# Testando com Trie
wordDictionary = WordDictionary()
for palavra in palavras:
    wordDictionary.addWord(palavra)

# Resultados da busca
for query in querys:
    print(wordDictionary.search(query))

end = time.time()
print(f'TEMPO DE EXECUCAO {end-start:.7f}')