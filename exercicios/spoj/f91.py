def f91(n):
  if n <= 100:
    return n-10
  else:
    return 91
res = []
ns = []
while True:
  n = int(input())
  if n == 0:
    break
  print(f'f91({n}) = {f91(n)}')
