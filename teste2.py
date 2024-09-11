import time

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
    
    def update(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += index & -index
    
    def prefix_sum(self, index):
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total

# Ler a entrada do arquivo
with open('test.txt', 'r') as file:
    input_data = file.read().splitlines()

# Extrair n e q
n, q = map(int, input_data[0].split())

# Inicializar Fenwick Tree
fenwick_tree = FenwickTree(n)

# Inicializar o array 'elementos' com zeros e aplicar atualização inicial
elementos = [0] * n
for i in range(n):
    fenwick_tree.update(i + 1, elementos[i])

# Extrair consultas
queries = [line.split() for line in input_data[1:]]

# Medir tempo de execução
start_time = time.perf_counter()

results = []
for query in queries:
    if query[0] == '1':
        # Prefixo, a consulta é na posição (query[1])
        index = int(query[1])
        results.append(fenwick_tree.prefix_sum(index))
    elif query[0] == '2':
        # Atualização, a consulta é na posição (query[1]) com o valor query[2]
        index = int(query[1])
        valor = int(query[2])
        # Atualizar o Fenwick Tree
        fenwick_tree.update(index, valor - elementos[index - 1])
        elementos[index - 1] = valor

# código a ser medido
end_time = time.perf_counter()

# Imprimir resultados
for result in results:
    print(result)

print(f"Tempo de execução: {end_time - start_time:.6f} segundos")
