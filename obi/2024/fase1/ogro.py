#E dedos na mao esquerda
#D dedos na mao direita
# se E>D, RESULTADO = E+D
# se D>E, RESULTADO = 2*(D-E)

e = int(input("").strip())
d = int(input("").strip())

if (d > 5 or e > 5) or (d < 0 or e < 0):
    raise Exception("Quantidade de dedos invalida")

def calcular_resultado():
    resultado = 0
    if e > d:
        resultado = e+d
    elif e < d:
        resultado = 2*(d-e)
    elif e == d:
        raise Exception("Quantidade de dedos invalida")
    return resultado

print(calcular_resultado())