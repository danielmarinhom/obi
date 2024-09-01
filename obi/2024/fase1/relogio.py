h = int(input().strip())
m = int(input().strip())
s = int(input().strip())

t = int(input().strip())

def calcular_hora():
    segundos_totais = s + m * 60 + h * 60 * 60 + t
    horas = segundos_totais // 3600
    minutos = (segundos_totais % 3600) // 60
    segundos = (segundos_totais % 3600) % 60

    # Verifica se há necessidade de ajustar as horas
    horas %= 24

    print(horas)
    print(minutos)
    print(segundos)

calcular_hora()