import time
#n, j
'''
n, j = map(int,input().split()) 
palavras = [input() for _ in range(n)]
querys = [input() for _ in range(j)]
print(palavras)
print(querys)
'''
start = time.time()
n, j = 10, 10
palavras = [
    "supercalifragilisticexpialidociou",
    "pseudopseudohypoparathyroidis",
    "floccinaucinihilipilificatio",
    "antidisestablishmentarianis",
    "honorificabilitudinitatibu",
    "thyroparathyroidectomizedd",
    "dichlorodifluoromethanee",
    "incomprehensibilitiessss",
    "psychoneuroendocrinologica",
    "hepaticocholangiocholecystentero"
]

# Consultas longas ajustadas
querys = [
    "supercali......isticexpialidociou",
    "pseudop.....hypoparathyroidis",
    "floccinaucini...ipllificatio",
    "anti...establis.mentarianis",
    "hono..ficab..itudi..tatibu",
    "thyrop......roidectomizedd",
    "dichlorodi......methanee",
    "incom.rehensibilitie....",
    "psycho.euroendocrino......",
    "hepa.icocholang.ochole..stentero"
]
def search(palavras, query):
  valido = [True]*len(palavras)
  for j, palavra in enumerate(palavras):
    for i in range(len(query)):
      if len(palavra) != len(query):
        valido[j] = False
        continue
      elif query[i] != '.' and query[i] != palavra[i]:
        valido[j] = False
  return True if True in valido else False
res = []
for q in querys:
  res.append(search(palavras, q))
end = time.time()
for j in res:
  print(j)
print(f'TEMPO DE EXECUCAO {end-start:.7f} segundos')
'''
3 4
bad
dad
mad
pad
bad
.ad
b..
'''