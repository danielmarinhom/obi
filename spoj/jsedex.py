diametro = int(input())
caixa = list(map(int,input().split()))
def cabe(caixa, diametro):
  for valor in caixa:
    if valor < diametro:
      return "N"
  return "S"

print(cabe(caixa,diametro))
  