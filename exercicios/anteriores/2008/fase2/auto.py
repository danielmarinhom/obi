#defletroes em blocos continuos  de 10 metros de extensao
#P-Pista, trecho em linha reta sem curvas ou saidas (um em cada lado)
#C-Curva, trecho em curva de 90 graus (dois paineis do lado externo, o outro fica sem)
#A-Acesso, trecho em linha reta, no qual existe uma entrada/saida a partir de um dos lados (um painel no lado onde NAO existe o acesso)
#D-Duplo acesso, linha reta com dois acessos, (nenhum painel deve ser instalado)

#C = 1 <= C <= 10**6 - comprimento da estrada em blocos de 10metros
#C caracteres, cada letra descrevendo um bloco de 10metros

#unidades de paineis

c = int(input())
operacoes = []
l = input()
for letra in l:
  operacoes.append(letra)

def calcular_paineis(operacoes, c):
  res = 0
  for i in range(c):
    if operacoes[i] == 'P' or operacoes[i] == 'C':
      res+=2
    if operacoes[i] == 'A':
      res+=1
  return res

print(calcular_paineis(operacoes, c))
