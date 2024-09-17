from collections import deque

def is_adjacent(word1, word2):
    """Função que verifica se duas palavras diferem por exatamente uma letra."""
    diff_count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff_count += 1
        if diff_count > 1:
            return False
    return diff_count == 1

def bfs(start, end, word_list):
    # Conjunto de palavras válidas
    word_set = set(word_list)
    
    # Fila de BFS (contendo tuplas: palavra atual, número de passos)
    queue = deque([(start, 1)])
    
    # Conjunto de palavras visitadas para evitar ciclos
    visited = set([start])
    
    while queue:
        word, steps = queue.popleft()
        
        # Se alcançamos a palavra final, retornamos o número de passos
        if word == end:
            return steps
        
        # Gerar todas as palavras adjacentes e validá-las
        for next_word in list(word_set):
            if is_adjacent(word, next_word) and next_word not in visited:
                visited.add(next_word)
                queue.append((next_word, steps + 1))
    
    # Se não houver caminho possível, retorne -1
    return -1

# Exemplo de uso
start_word = "hit"
end_word = "cog"
word_list = ["hot", "dot", "dog", "lot", "log", "cog"]

result = bfs(start_word, end_word, word_list)
print(f"Menor número de transformações: {result}")
