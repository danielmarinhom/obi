
n = int(input())
placares = []
for _ in range(n):
  x,y = map(int,input().split())    #x a favor   y contra
  placares.append((x,y))
#i e j, a primeira e ultima partidas do melhor periodo, se for 0, deve ser "nenhum"

