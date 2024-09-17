def compute_prefix_function(p):
  m = len(p)
  pi = [0] * m
  k = 0
  for q in range(1, m):
    while k > 0 and p[k] != p[q]:
      k = pi[k - 1]
    if p[k] == p[q]:
      k += 1
    pi[q] = k
  return pi

#PROCURAR PADROES
def kmp_search(t, p):
  n = len(t)
  m = len(p)
  pi = compute_prefix_function(p)
  q = 0
  positions = []
  for i in range(n):
    while q > 0 and p[q] != t[i]:
      q = pi[q-1]
    if p[q] == t[i]:
      q += 1
    if q == m:
      positions.append(i - m + 1)
      q = pi[q-1]
  return positions

#"abcde" é uma rotação de "cdeab" pois "abcde esta em "cdeab"+"cdeab"
def is_rotating(s1, s2):
  if len(s1) != len(s2):
    return 0
  combined = s1 + s1
  return kmp_search(combined, s2) != []
def is_rotating2(s1,s2):
  if len(s1) != len(s2):
    return False
  return s2 in (s1 + s1)
print(is_rotating("abcd", "abcd"))  # Output: True
print(is_rotating("abcd", "abdc"))  # Output: False

# menor substring que, quando repetida, forma a string original.
# Por exemplo, a string "ababab" tem um período de "ab", pois "ab" repetido 3x
# resulta em "ababab"
def find_period(s):
  pi = compute_prefix_function(s)
  n = len(s)
  period_length = n - pi[-1]
  if n % period_length == 0:
    return period_length
  else:
    return n
#