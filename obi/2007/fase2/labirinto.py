#N linhas e M colunas
#cada celula possui uma plataforma, que varia de 0(mais baixa) a 9(mais alta)
#voce inicia em (1,1)
#objetivo = chegar em (N)(M)
#se a celula estiver entre duas ou mais unidades acima da sua altura atual, voce nao pode move-lo
#a cada turno voce pode mover para uma das 4 celulas adjacentes
#caso a altura da celula destino seja menor ou igual a sua celula + 1
#a cada turno cada celula aumenta 1 unidade ate o valor maximo (9), se for 9 devera ser 0
#o jogador pode decidir esperar subir as plataformas

nm = input().split()
a = list(map(int,nm))
n, m = a[0], a[1]
matriz = [[] for _ in range(n)]

for i in range(n):
  linha = input("").split()
  for j in range(m):
    matriz[i].append(int(linha[j]))

def aumentar_plataforma(matriz, n, m):
  for i in range(n):
    for j in range(m):
      if matriz[i][j] < 9:
        matriz[i][j] += 1
      elif matriz[i][j] == 9:
        matriz[i][j] = 0
def achar_saida(matriz, n,m ):
  objetivo = [n-1, m-1]
  atual = [0,0]
  res = 0
  while atual != objetivo:
    for i in range(n):  #altura
      for j in range(m):  #largura
        print(atual)
        if i < (atual[0] + 1) and atual != objetivo:
          atual[0] = matriz[i][0]
          atual[1] = matriz[i][1]
          res += 1
          aumentar_plataforma(matriz, n, m)
    
  return res
print(achar_saida(matriz, n, m))