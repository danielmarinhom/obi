def mdc(a, b):
  while b != 0:
    a,b = b, a % b
  return a

def mmc(a, b):
  return abs(a*b) // mdc(a, b)


print(mdc(6, 4))
print(mmc(6, 4))
#print(mdc(480002, 18345682)) 