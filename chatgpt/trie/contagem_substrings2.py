# String de teste
s = "abcabcabcd"

# Abordagem com itertools.permutations
import time
from itertools import permutations

start_time = time.time()
permutas = set()
for perm in permutations(s):
    permutas.add(perm)
end_time = time.time()
print(f"Usando itertools.permutations: {len(permutas)} permutações únicas")
print(f"Tempo de execução: {end_time - start_time:.2f} segundos")

# Abordagem com math.factorial e Counter
import math
from collections import Counter

def count_unique_permutations(s):
    freq = Counter(s)
    n = len(s)
    numerator = math.factorial(n)
    denominator = 1
    for count in freq.values():
        denominator *= math.factorial(count)
    return numerator // denominator

start_time = time.time()
unique_permutations = count_unique_permutations(s)
end_time = time.time()
print(f"Usando math.factorial e Counter: {unique_permutations} permutações únicas")
print(f"Tempo de execução: {end_time - start_time:.2f} segundos")
