import math
import time
start1 = time.time()
n = int(input())
print(math.factorial(n))
end1 = time.time()

start2 = time.time()
def fatorial(n):
  atual = n
  while n > 1:
    n -= 1
    atual *= n
  return atual
print(fatorial(n))
end2 = time.time()
print(f'{end1-start1:.7f} segundos')
print(f'{end2-start2:.7f} segundos')