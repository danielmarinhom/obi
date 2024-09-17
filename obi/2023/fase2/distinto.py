n = int(input())
digitos = []
for _ in range(n):
  digitos.append(input())

def retornar_sequencia(digitos):
  sequencia = ''
  for i in range(len(digitos)):
    if digitos[i] not in sequencia:
      sequencia += digitos[i]
  
  return len(sequencia)
print(retornar_sequencia(digitos))