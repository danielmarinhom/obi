def premiado(ingressos):
  for i in range(len(ingressos)):
    if i == ingressos[i]-1:
      return i+1

respostas = []
while True:
  n = int(input())
  if n == 0:
    break    
  ingressos = list(map(int,input().split()))
  respostas.append(premiado(ingressos))

for i, numero in enumerate(respostas):
  print(f"Teste {i+1}")
  print(numero)
  print()