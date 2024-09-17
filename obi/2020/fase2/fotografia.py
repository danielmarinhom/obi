#a fotografia seja inteiramente contida dentro da moldura
#a area da moldura nao ocupada pela fotografia seja a menor possivel
#nao pode ser rotacionado, lados da foto devem ser paralelos aos da moldura

#A, L - altura e largura da fotografia em CM
#N - quantidade de molduras

#moldura mais perto de 0 pelo indice, se nenhuma, -1

al = input("").split()
a, l = int(al[0]), int(al[1])
n = int(input(""))
molduras = []
for i in range(n):
  x = input("").split()
  y = list(map(int, x))
  molduras.append(y)

def moldura_certa(molduras, n, a, l):
  melhor_moldura = -1
  menor_area = 0
  for i in range(n):
    xi, yi = molduras[i]
    if (a <= xi and l <= yi) or (a <= yi and l <= xi):
      area_nao_ocupada = xi*yi - a*l
      if area_nao_ocupada < menor_area:
        menor_area = area_nao_ocupada
        melhor_moldura = i+1
  return melhor_moldura

print(moldura_certa(molduras, n, a, l))


  
