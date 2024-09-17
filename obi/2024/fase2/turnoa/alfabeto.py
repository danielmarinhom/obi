k, n = map(int,input().split()) # caracteres no alfabeto alien, numero de caracteres
alienigina = input()
mensagem = input()

def isalien():
    trues = 0
    for i, letra in enumerate(mensagem):
        if letra in alienigina:
            trues += 1
    return "N" if trues != len(mensagem) else "S"
print(isalien())