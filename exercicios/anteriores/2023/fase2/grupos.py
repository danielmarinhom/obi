#grupos de 3 estudantes
#lista de pares que gostariam de estar no mesmo grupo euma dos que nao gostariam de estar no mesmo
#o numero total de restricoes que sao violadas com essa distribuicao

#E,M,D - numero de estudantes, numero de pares que gostariam de estar no mesmo grupo, dos que nao
##estudantes sao identificados por 1 a E
#M linhas seguintes descreve um par que gostariam de estar juntos, X e Y
#D linhas seguintes descreve um par que nao gostariam de estar juntos, U e V
#cada uma das E/3 linhas seguintes descreve um grupo de estudantes, I,J,K, estudantes

#total de restriccoes que sao violadas nos grupos da entrada

e,m,d = map(int,input().split())
juntos = []
separados = []
grupos = []
for _ in range(m):
  x,y = map(int,input().split())
  juntos.append((x,y))
for _ in range(d):
  u,v = map(int,input().split())
  separados.append((u,v))
for _ in range(e//3):
  i,j,k = map(int,input().split())
  grupos.append((i,j,k))

def verificar_restricoes(juntos,separados, grupos):
  res = 0
  for x,y in juntos:
    for grupo in grupos:
      if x in grupo and y in grupo:
        juntos.remove((x,y))
  res += len(juntos)

  for x,y in separados:
    for grupo in grupos:
      if x in grupo and y in grupo:
        separados.remove((x,y))
  res += len(separados)
  return res

print(verificar_restricoes(juntos, separados, grupos))