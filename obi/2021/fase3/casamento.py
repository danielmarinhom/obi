#fazemos A e B terem o mesmo numero de digitos adicionando zero a esquerda
#cada digito de A eh comparado com o correspondente de B, e de menor valor eh eliminado
#se forem iguais mantem
#caso nao haja nenhum restante, retornar -1

a = int(input())
b = int(input())

def casamento(a,b):
  while len(a) != len(b):
    if len(a) > len(b):
      temp = b[0]
      b[0] = 0
      for i in range(len(b)):
        b[i] = b[i+1]
      b[0] = 0
    if len(a) < len(b):
      numeros[2].insert(0,0)
  return(numeros)

print(casamento(numeros))