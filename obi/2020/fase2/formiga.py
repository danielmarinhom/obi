#cada tunel conecta dois saloes
#so pode escorregar se I esta maior que J

#S, T, P, numero de saloes, tuneis, e o salao do qual sera a partida (1 a S)
#Ai, a altura em que o salao i esta no formigueiro
#T linhas seguintes, tem dois inteiros I e J indicando que ha um tunel entre I e J

stp = input("").strip().split()
S, T, P = int(stp[0]), int(stp[1]), stp[2]
alt = input("").split()
alturas = list(map(int, alt))
tuneis = []
for i in range(T):
  x = input("").split()
  tuneis.append(x)
print(tuneis)
print(alturas)
def maior_numero(tuneis, alturas):
  altura_atual = alturas[int(P)-1]
  salao_atual = P
  contador = 0
  

print(maior_numero(tuneis, alturas))



