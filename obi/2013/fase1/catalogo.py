#N, arquivos joyce possui no DVD
#Descricao de um arquivo a partir da raiz

#minimo de caracteres para descrever o catalogo

n = int(input(" > "))
m = []
for _ in range(n):
  m.append(input(" > "))

def extrai_raiz(m):
  main_dir = []
  for elemento in enumerate(m):
    x = elemento[1]
    listaX = x.split("/")
    x = listaX[0]
    main_dir.append(x)
  return main_dir

#calcula o diretorio raiz mais repetido
def mais_repetido(main_dir:list):
  mais_repetido = ''
  for i in range(len(main_dir)):
    vezes_repetido = main_dir.count(main_dir[0])
    mais_repetido = main_dir[0]
    if main_dir.count(main_dir[i])  > vezes_repetido:
      vezes_repetido = main_dir.count(main_dir[i])
      mais_repetido = main_dir[i]
  return mais_repetido

mais_repetido(main_dir=extrai_raiz(m))
#onde o mais repetido aparece, apaga, onde nao aparece adiciona um ../ no comeco
#soma caracteres

#pegar 

novalista = []
for i in range(len(m)):
  x = m[0].split('/')
  if x[0] == mais_repetido:
    x.pop(0)
  else:
    x.



  