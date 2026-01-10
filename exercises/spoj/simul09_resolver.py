#inversao e soma
#inversao: dados dois enderecos, x e y, inverte a posicao de palavras da memoria de forma que
  #a palavra no endereco x troca com a da posicao y
  #a palavra em x+1 troca com y-1
  #a palavra em x+2 troca com y-2
  #ate que x>=y
#soma: dado dois enderecos de memoria x e y
#imprime a soma das palavras de memoria entre os enderecos x e y (inclusive)
#import sys
#input = sys.stdin.read


def inversao(lista, x,y):
  while x < y:
    lista[x-1], lista[y-1] = lista[y-1], lista[x-1]
    x+=1
    y-=1

def soma(lista, x,y):
  return sum(lista[x-1:y])

n,m = map(int,input().split())
lista = [i for i in range(1, n + 1)]
instrucoes = []
for _ in range(m):
  dx = input().split()
  op, x, y = dx[0], int(dx[1]), int(dx[2])
  instrucoes.append((op, x, y))

for op, x, y in instrucoes:
  if op == 'I':
    inversao(lista, x, y)
  elif op == 'S':
    print(soma(lista, x, y))

  
