def eratostenes(n):
  primos = [True] * (n+1)
  primos[0] = primos[1] = False
  p = 2
  while p*p <= n:
    if primos[p]:
      for i in range(p*p, n+1, p):
        primos[i] = False
    p += 1
  primes = [p for p in range(n+1) if primos[p]]
  return primes

def intervalo(a, b):
  primes = eratostenes(b)
  intervalo = [i for i in range(a,b+1) if i in primes]
  return intervalo


a,b = map(int,input().split())
print(intervalo(a,b))
