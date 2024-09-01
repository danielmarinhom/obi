#salas numeradas a partir de 1
#esquerda = 2*i
#direita = 2*i+1

n = int(input())
passos = input()

def esquerda(i):
    return 2*i
def direita(i):
    return 2*i+1

x = 1
for i, step in enumerate(passos):
    if step == 'E':
        x = esquerda(x)
    else:
        x = direita(x)
print(x)