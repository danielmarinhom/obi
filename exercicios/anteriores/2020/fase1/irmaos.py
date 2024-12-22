#N, idade de oscar
#M, idade de otavio
#R, idade de orlando

#orlando
#otavio
#oscar

#otavio - oscar = orlando - otavio
#m - n = r - m

n = int(input(" > "))
m = int(input(" > "))


def calcular_r(n:int, m:int):
  return (m-n)+m

print(calcular_r(n, m))