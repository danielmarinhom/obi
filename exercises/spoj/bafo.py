
def vencedor(resultados):
  aldo_pontos = 0
  beto_pontos = 0
  for aldo, beto in resultados:
    vencedor = max(aldo,beto)
    if aldo == vencedor:
      aldo_pontos += 1
    else:
      beto_pontos += 1
  return "Aldo" if aldo_pontos > beto_pontos else "Beto"
  

respostas = []
while True:
  r = int(input())
  if r == 0:
    break
  resultados = []
  for _ in range(r):
    aldo, beto = map(int,input().split())
    resultados.append((aldo,beto))
  respostas.append(vencedor(resultados))

for i, resposta in enumerate(respostas):
  print(f"Teste {i+1}")
  print(resposta)
  print()