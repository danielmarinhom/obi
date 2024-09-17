#N, M, numero de ingredientes e o numero de pares que nao combinam
#linhas seguintes sao pares que nao combinam

nm = input("").split()
n, m = int(nm[0]), int(nm[1])

ingredientes = [i for i in range(n)]

ncombinam = [[0] for _ in range(m)]
for i in range(m):
  x = input("").split()
  ncombinam.append(x)

combinacoes = []
for i in range(n):
  par = []
  for l in range(len(par)):
    for k in range(m):
      if not par[i] in ncombinam[k]:
        combinacoes.append(par[i])
  for j in range(n):
    par.append(ingredientes[i][j])

print(len(combinacoes))
  
