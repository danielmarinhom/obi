#S, T - numero de saloes, numero de tuneis
#cada T linha descreve um tunel de sala X e Y
#p = int(input()) # numero de sugestoes de passeio
#p linhas descreve uma sugestao de passeio 

s,t = map(int,input().split())
conexoes = []
for _ in range(t):
  x,y = map(int,input().split())
  conexoes.append((x,y))

p = int(input())
sugestoes = []
for _ in range(p):
  sugestao = list(map(int,input().split()))
  sugestao.pop(0)
  sugestoes.append(sugestao)
for i in range(len(sugestoes)):
  sugestoes[i].pop(0)
def calcular_conexoes(conexoes, sugestoes):
  n = len(sugestoes)
  validas = [[True] for _ in range(n)]
  for i in range(len(sugestoes)):
    print("I:",i)
    for j in range(1,len(sugestoes[i])):
      nx = sugestoes[i][j-1]
      ny = sugestoes[i][j]
      if (nx,ny) not in conexoes and (ny,nx) not in conexoes:
        validas[i] = False

  return validas.count(True)

print(calcular_conexoes(conexoes, sugestoes))