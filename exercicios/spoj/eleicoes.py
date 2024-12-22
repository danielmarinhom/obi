n = int(input())
votos = {}
for _ in range(n):
  candidato = int(input())
  if candidato in votos:
    votos[candidato] += 1
  else:
    votos[candidato] = 1
vencedor = max(votos, key=votos.get)

print(vencedor)