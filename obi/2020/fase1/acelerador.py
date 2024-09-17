#1 2 3
#sai por uma das 3 saidas e atinge 1 sensor
#do emissor ate o acelerador, 3 km e a circunferencia, 8km

km = int(input(" > "))

inicial = 3#km
circunferencia=8#km

def calcular_voltas(km:str):
  km -= inicial
  if km < 8:
    if km == 6:
      return 1
    if km == 7:
      return 2
    if km == 8:
      return 3
  while km > 8:
    km -= 8
  if km < 0:
    return 0
  if km == 4:
    return 2
  if km == 3:
    return 1
  if km == 5:
    return 3
  
print(calcular_voltas(km))
