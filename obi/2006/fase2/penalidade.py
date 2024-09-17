#objetivo, do [0][0] ir para [n-1][n-1]
#um quadrado para baixo ou para direita a cada passo
#a peca nao pode ser colocada em nenhum quadrado com ZERO
#custo = todas as casas percorridas multiplicadas
#penalidade = quantidade de zeros da direita para esquerda
#PENALIDADE MINIMA

#
def custo_minimo(n,matriz):
  esquerda, direita, cima, baixo = 0, n, 0, n
  #no caso de um 3x3, [2][2]
  chegou = False
  while chegou != True:
    custo = 0
    


n = int(input(""))

matriz = [[0]*n for _ in range(n)]

for i in range(n):
  l = input("").split()
  matriz[n] = l


