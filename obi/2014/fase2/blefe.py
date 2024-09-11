#conjunto A fixo de N inteiros e sequencia de B vazia
#os jogadores dao append na B
#ou incluir em B qualquer um dos numeros do conjunto A
#ou incluir em B um numero que eh a soma de dois numeros que ja estejam em B (pode ser do mesmo num)

n,m = map(int,input().split()) #tamanho do A, tamanho de B
conjA = list(map(int,input().split()))
conjB = list(map(int,input().split()))

def verificar_jogadas(conjA,conjB):
  somas = set()
  for num in conjB:
    for num1 in conjB:
      somas.add(num+num1)
  print(somas)
  for jogada in conjB:
    if jogada not in conjA and jogada not in somas:
      return jogada
  return "sim"
print(verificar_jogadas(conjA, conjB))

#10 min