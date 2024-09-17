#um cavalo pode ser montado por varios policiais (com limites)
#um policial so monta um cavalo


def soldados_cavalos(afinidades, pode_montar, num_soldados):
  res = 0
  montados = [0]*len(pode_montar)
  for i in range(num_soldados):
    for u,v in afinidades:
      if i == v and pode_montar[u] < montados[u]:
        res += 1
        montados[u] += 1
  return res

def soldados__cavalos(afinidades,pode_montar,num_soldados, num_cavalo):#m,n
  alocacao = [-1] * (num_soldados+1)
  capacidade_cavalos = pode_montar[:]
  alocados = 0
  for cavalo, soldado in afinidades:
    if alocacao[soldado] == -1 and capacidade_cavalos[cavalo-1] > 0:
      alocacao[soldado] = cavalo
      capacidade_cavalos[cavalo-1] -= 1
      alocados += 1
  return alocados


n,m,k = map(int,input().split()) #n - num cavalos, m - num soldados, k - num afinidades
pode_montar = list(map(int,input().split()))
afinidades = []
for _ in range(k):
  u,v = map(int,input().split())  #cavalo, soldado
  afinidades.append((u,v))
print("Instancia 1")
print(soldados__cavalos(afinidades,pode_montar,m,n))
respostas = []
while True:
  n = int(input())
  if n == 0:
    break    
  ingressos = list(map(int,input().split()))
  respostas.append(premiado(ingressos))

for i, numero in enumerate(respostas):
  print(f"Teste {i+1}")
  print(numero)
  print()
print(soldados__cavalos(afinidades, pode_montar, m, n))