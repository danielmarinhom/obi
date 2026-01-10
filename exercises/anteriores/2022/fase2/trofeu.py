#5 trofeus (empate, todos com mesma pontuacao)
#1 trofeu (maior pontuacao) 2 placas (empate na segunda maior posicao)
#2 trofeus (empate na maior posicao) 2 placas (empate na segunda maior posicao)

#trofeus e placas
notas = [int(input()) for _ in range(5)]
trofeus, placas = 0, 0
def calcular_trofeus(notas):
  maior = notas[0]
  segunda_maior = -1
  trofeus = notas.count(maior)
  for p in notas:
    if p < maior:
      segunda_maior = p
      break
  num_placas = notas.count(segunda_maior) if segunda_maior != -1 else 0
  return trofeus, num_placas
    
trofeus, placas = calcular_trofeus(notas)
print(trofeus, placas)
