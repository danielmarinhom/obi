import math
from collections import Counter

s = input().strip()
n = len(s)
char_count = Counter(s)
print(char_count)
permuta = math.factorial(n)
for count in char_count.values():
  print(permuta, math.factorial(count))
  permuta //= math.factorial(count)

print(permuta-1)
