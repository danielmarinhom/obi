#I1 e I2 - interruptores
#ao apertar I1, a lampada A accende se estiver apagada e apaga se estiver acesa
#se apertar I2 cada uma das lampadas A e B troca de estado

#N - quantidade de apertadas
#1 para I1 2 para I2

#estado da A
#estado da B

a = 0
b = 0

def int1(lampada1):
  if lampada1 == 1:
    return 0
  else:
    return 1

def int2(lampada1, lampada2):
  lampadas = [lampada1, lampada2]
  for i in range(len(lampadas)):
    if lampadas[i] == 1:
      lampadas[i] = 0
    else:
      lampadas[i] = 1
  return lampada1, lampada2

n = int(input(""))

x = input().split()
comandos = list(map(int, x))
for comando in comandos:
  if comando == 1:
    a = int1(a)
  else:
    a, b = int2(a, b)
print(a)
print(b)