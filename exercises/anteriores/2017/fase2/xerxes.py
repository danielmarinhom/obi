#dario e xerxes
#n rodadas
#cada jogador escolhe uma mao entre 5 opcoes #indice 0

n = int(input())
maos = []
for _ in range(n):
  d,x = map(int,input().split())
  maos.append((d,x))
relacoes = {
  0: [1,2],
  1: [2,3],
  2: [3,4],
  3: [0,4],
  4: [0,1],
}
def vencedor(relacoes, maos):
  pontuacoes = [0,0] #xerxes, dario
  for dario, xerxes in maos:
    if xerxes in relacoes[dario]:
      pontuacoes[1] += 1
    elif dario in relacoes[xerxes]:
      pontuacoes[0] += 1
  return "dario" if pontuacoes[1] > pontuacoes[0] else "xerxes"

print(vencedor(relacoes, maos))

#aprox 8 minutos