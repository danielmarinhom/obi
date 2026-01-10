#matriz

#N linhas
#N colunas
#1, viva
#0, morta
#1 celula tem 8 vizinhas

#celula 0 tem 3 vizinhas 1, celula = 1 
#celula 0 tem != 3 vizinhas, celula = 0
#celula 1 tem 2 ou 3 vizinhas 1, celula = 1
#celula 1 tem menos que 2 vizinhas 1, celula = 0
#celula 1 tem mais que 3 vizinhas 1, celula = 0

#N, Q - N, linhas/colunas - Q, passos a serem simulados
#

n, q = input("").strip().split()
n, q = int(n), int(q)

matriz = []

for i in range(n):
    x = input("").strip().split()
    matriz.append(x)

print(matriz)
print("----")

def calcular_geracao():

    def calcular_morto():
        for linha in matriz:
            for i, elemento in enumerate(linha):
                vizinhosUm = 0
                if elemento == '0':
                    if linha == matriz[0]:
                        if i == len(linha):
                            if linha[i-1] == '1':
                                vizinhosUm+=1
                            if linha+1[i] == '1':
                                vizinhosUm+=1
                            if linha+1[i-1] == '1':
                                vizinhosUm+=1
                        elif i == 0:
                            if linha[i+1] == '1':
                                vizinhosUm+=1
                            if linha+1[i] == '1':
                                vizinhosUm+=1
                            if linha+1[i+1] == '1':
                                vizinhosUm+=1
                        else:
                            if i == 0:
                                if linha[i+1] == '1':
                                    vizinhosUm+=1
                                if linha+1[i] == '1':
                                    vizinhosUm+=1
                                if linha-1[i] == '1':
                                    vizinhosUm+=1
                                if linha+1[i+1] == '1':
                                    vizinhosUm+=1
                                if linha-1[i-1] == '1':
                                    vizinhosUm
                            elif i == len(linha):
                                if linha[i-1] == '1':
                                    vizinhosUm+=1
                                if linha+1[i] == '1':
                                    vizinhosUm+=1
                                if linha-1[i] == '1':
                                    vizinhosUm+=1
                                if linha+1[i-1] == '1':
                                    vizinhosUm+=1
                                if linha-1[i-1] == '1':
                                    vizinhosUm
                            else:
                                if linha[i+1] == '1':
                                    vizinhosUm+=1
                                if linha[i-1] == '1':
                                    vizinhosUm+=1
                                if linha+1[i+1]:
                                    vizinhosUm+=1
                                if linha+1[i-1]:
                                    vizinhosUm+=1
                                if linha-1[i-1]:
                                    vizinhosUm+=1
                                if linha-1[i+1]:
                                    vizinhosUm+=1
                if vizinhosUm == 3:
                    linha[i] == '1'
                             
    calcular_morto()
