cartas = list(map(int,input().split()))
def ordenada(cartas):
  if cartas == sorted(cartas):
    return "C"
  elif cartas == sorted(cartas, reverse=True):
    return "D"
  else:
    return "N"
print(ordenada(cartas))