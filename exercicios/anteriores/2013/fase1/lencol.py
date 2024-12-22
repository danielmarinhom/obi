#dimensoes axb
#6 inteiros, A1, B1, A2, B2, A e B
#dimensoes dos dois retangulos e as dimensoes do retangulo desejado

#S ou N
a1, b1, a2, b2, a, b = map(int, input(" > ").split())


def verificar_p(p1:int, p2:int, pab:int):
  if p1 == pab or p2 == pab:
    print("S")
  else:
    print("N")
pab = abs((a+b)*2)
verificar_p(abs((a1+b1)*2), abs((a2+b2)*2), pab)

verificar_p(abs((a1+b2)*2), abs((a2+b1)*2), pab)

verificar_p(abs((b2+a2)*2), abs((a2+b1)*2), pab)
