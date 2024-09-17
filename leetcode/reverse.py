def reverse(x):
  negative = x < 0
  x = abs(x)
  rev = int(str(x)[::-1])
  return 0 if rev >= 2**31 else -rev if negative else rev