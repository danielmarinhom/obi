#vendedores identificados de 1 a N
#todos estao inativos
#ele ficara T minutos para aquela ligacao
#o tempo entre ligacoes eh desprezivel
#nao pode fazer mais de uma ao mesmo tempo
#o vendedor inativo deve fazer a do topo da lista (caso mais de um inativo, o com menor id faz o do topo)
#a ligacao eh removida depois de ser atendida
#quando a ligacao eh terminada o atendente fica inativo

#N e L - numero de vendedores e de ligacoes
#L linhas, T duracao de cada ligacao

#I e P numero do vendedor (de 1 a N) e o numero de ligacoes

x = input("").split()
n, l = int(x[0]), int(x[1])

ligacoes = []
atendentes = [[0] for _ in range(n)]

for i in range(l):
  y = int(input(""))
  ligacoes.append(y)


for i in range(len(atendentes)):
  print(atendentes)
  if atendentes[i][0] == 0:
    if ligacoes:
      atendentes[i].append(ligacoes.pop(0))
      atendentes[i] = 1
  else:
    proximo = 31
    for j in range(len(atendentes)):
      for k in range(len(atendentes[j])):
        if atendentes[i][-1] < 0:
          proximo = atendentes[i][0]
    if ligacoes:
      atendentes[i].append(ligacoes.pop(0))
      atendentes[i] = 1



resultados = []

for i in range(len(atendentes)):
  soma = 0
  resultados.append(soma)
  for j in range(1,len(atendentes[i])):
    soma += 1

print(soma)
