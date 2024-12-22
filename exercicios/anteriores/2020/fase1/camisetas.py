n = int(input(" > "))
t = input(" > ").strip()
p = int(input(" > "))
m = int(input(" > "))

lista_solicitados = t.split()

pequenas_solicitadas = 0
medias_solicitadas = 0

for numero in lista_solicitados:
  if int(numero) == 1:
    pequenas_solicitadas += 1
  if int(numero) == 2:
    medias_solicitadas += 1

def verificar_disponibilidade():
  if pequenas_solicitadas == p and medias_solicitadas == m:
    return "S"
  else:
    return "N"
  
print(verificar_disponibilidade())
#segundo ex em 32:29.22
