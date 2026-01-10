

def aeroport(aeroportos):
  lens = []
  lenmaximo = 0
  for i in range(len(aeroportos)):
    if len(aeroportos[i]) > lenmaximo:
      lens.append((i+1,len(aeroportos[i])))

  lens.sort(key= lambda x:x[1], reverse=True)
  maximo = lens[0][1]
  res = ""
  for u,v in lens:
    if v == maximo:
      res += str(u) + " "
  return res


respostas = []
while True:
  a,v = map(int,input().split()) #aeroportos, voos

  if a == 0 and v == 0:
    break 

  voos = []
  for _ in range(v):
    x,y = map(int,input().split())
    voos.append((x-1,y-1))
  aeroportos = [[0] for _ in range(a)]
  for a1, a2 in voos:
    aeroportos[a1].append(a2)
    aeroportos[a2].append(a1)
  respostas.append(aeroport(aeroportos))
  
for i, numero in enumerate(respostas):
  print(f"Teste {i+1}")
  print(numero)
  print()



