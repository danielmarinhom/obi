n = int(input())
clientes = []
for _ in range(n):
  inicio, termino = map(int, input().split())
  clientes.append((inicio, termino))

# Ordena os clientes pelo horário de término
clientes.sort(key=lambda x: x[1])

tempo_atual = 0
semSobr = 0

for inicio, termino in clientes:
  if inicio >= tempo_atual:
    semSobr += 1
    tempo_atual = termino

print(semSobr)