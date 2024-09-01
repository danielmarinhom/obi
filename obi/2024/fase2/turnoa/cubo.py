#NxNxN cm
#cortou o cubo em n**3 de lado 1cm (1x1x1)
#ou tem 0, 1, 2 ou 3 pintadas

#entre 64 cubinhos, 8 nao tinham nenhuma, 24 1, 8 com 3
import math

n = int(input())

def faces(n):
    cubinhos = n**3
    nn = n*2
    c2 = nn + (n*3)
    c3 = n*2
    c1 = n
    c0 = cubinhos - (c1+c2+c3)
    return c0, c1, c2, c3



c0, c1, c2, c3 = faces(n)
res = [c0, c1, c2, c3]
for x in res:
    print(x)