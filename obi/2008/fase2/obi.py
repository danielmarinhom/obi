#o total de pontos de um competidor eh a soma dos pontos obtidos nas duas fases

#N e P - competidores e pontos minimos
#N linhas contem X e Y - pontuacao em cada fase

#numero de competidores 

n,p = map(int,input().split())
competidores = []
for _ in range(n):
  x,y = map(int,input().split())
  competidores.append((x,y))
def calcular_competidores(competidores, minimo):
  notas = []
  res = 0
  for x,y in competidores:
    notas.append(x+y)
  for nota in notas:
    if nota >= minimo:
      res += 1
  return res
print(calcular_competidores(competidores, p))