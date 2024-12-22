h = int(input("").strip())
m = int(input("").strip())
s = int(input("").strip())

t = int(input("").strip())
if t > (10**5):
    raise Exception("T EXCEDE O LIMITE")
def calcular_tempo():
    segundos = h*3600 + m*60 + s + t
    while segundos >= 86400:
        segundos -= 86400 
    minutos, horas = 0, 0
    while segundos >= 60:
        minutos += 1
        segundos -= 60
    while minutos >= 60:
        horas += 1
        minutos-=60
    print(horas)
    print(minutos)
    print(segundos)

calcular_tempo()