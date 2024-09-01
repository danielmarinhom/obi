#estradas bidirecionais
#se ha um caminho entre qualquer par de zonas

#N e M - numero de zonas, numero de estradas
#proximas M linhas contem U e V, indicando que ha uma estrada entre a zona U e a zona V

#Conectada se todas estao conectadas

#leitura dos dados
#leitura e append das estradas para cada dict {}
#roda o dicionario e verifica se tem um valor de chave+1




n, m = list(map(int, input().split()))
estradas = []
relacoes = {i: [] for i in range(n)}
for _ in range(m):
  u, v = map(int, input().split())
  estradas.append((u, v))
  relacoes[u].append(v)
  relacoes[v].append(u)

for i in range(len(estradas)):
  for x, y in enumerate(estradas[i]):
    relacoes[x].append(estradas[i][y-1])
    relacoes[y].append(estradas[i][x-1])

def verificar():
  for i, keys in enumerate(relacoes.keys()):
    if not keys+1 in relacoes[i]:
      return "Desconectada"
  return "Conectada"

print(verificar())