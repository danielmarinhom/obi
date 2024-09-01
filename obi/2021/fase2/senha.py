#para cada letra borrada -> escreve uma palavra com K letras
#escreveu um numero inteiro P
#para recuperar -> substitua cada letra borrada por uma das letras da respectiva lista, obtendo as possiveis senhas
#ordene em ordem lexicograficamente crescente
#a senha correta eh a P possivel senha na lista ordenada

#N, M, K, caracteres da senha, letras borradas, comprimento de cada palavra
#comprimento N, # representa letra borrada
#M linhas seguintes contem uma palavra, a S-esima palavra contem as letras para substituir a i-esima letra borrada
#P,o numero de ordem da senha

l = input("").strip().split()
N, M, K = int(l[0]), int(l[1]), int(l[2])

senha = input("")
if len(senha) != N:
  raise Exception()

palavras = []
for i in range(M):
  x = input("")
  palavras.append(x)

P = int(input(""))
#FIM DA LEITURA
combinacoes = []
indice = -1
for letra in senha:
  if letra == '#':
    indice += 1
    palavra = palavras[indice]
    for letter in palavra:
      novasenha = senha.replace(letra, letter)
      combinacoes.append(novasenha)
print(combinacoes[P-1])