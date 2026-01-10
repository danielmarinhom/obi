#50, 10, 5, 1

def retornar_notas(valor):
  notas = [50, 10, 5, 1]
  necessarios = [0, 0, 0, 0]
  
  for i in range(len(notas)):
    if valor >= notas[i]:
      necessarios[i] += valor//notas[i]
      valor = valor % notas[i]
    elif valor in notas:
      necessarios[notas.index(valor)] += 1
      break
  return " ".join(map(str,necessarios))

respostas = []
while True:
  valor = int(input())
  if valor == 0:
    break    
  respostas.append(retornar_notas(valor))

for i, numero in enumerate(respostas):
  print(f"Teste {i+1}")
  print(numero)
  print()