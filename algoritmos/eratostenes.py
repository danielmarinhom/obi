def eratostenes(n):
  primo = [True] * (n+1)
  primo[0] = primo[1] = False

  p = 2
  while p * p <= n:
    if primo[p]:
      for i in range(p*p, n+1, p):
        primo[i] = False
    p += 1
  primes = [p for p in range(n+1) if primo[p]]
  return primes
#a * p = 247 dois primos, p > a
def ap(primes):
  for i in range(len(primes)):
    for j in range(1,len(primes)):
      if primes[i] * primes[j] == 247:
        return f"{str(primes[i])} {str(primes[j])}" 
      
primes = eratostenes(247)
print(ap(primes))