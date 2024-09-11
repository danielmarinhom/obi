fibonacci_cache = {}

def fibonacci(n):
  value = 0
  if n in fibonacci_cache:
    return fibonacci_cache[n]
  if n <= 2:
    value = 1
  elif n > 2:
    value = fibonacci(n-1) + fibonacci(n-2)
  fibonacci_cache[n] = value
  return value 

for i in range(1000):
  print(f"{i} : {fibonacci(i)}")