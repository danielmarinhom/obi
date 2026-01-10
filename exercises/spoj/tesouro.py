#o valor dos objetos coletados por joao e por jose antes de encontrarem a arca
#uma lista de valores, correspondentes aos objetos encontrados dentro da arca
#sao dados em unidades de 1 mil


def divisao_possivel(objetos,soma):
  total = sum(objetos)
  if (total + soma) % 2 != 0:
    return "N"
  alvo = (total + soma) // 2
  dp = [False] * (alvo+1)
  dp[0] = True
  for valor in objetos:
    for j in range(alvo,valor-1,-1):
      if dp[j-valor]:
        dp[j] = True

  if dp[alvo]:
    return 'S'
  else:
    return 'N'



respostas = []
while True:
  x,y,n = map(int,input().split()) # x,y - soma dos valores antes dejoao e jose, n - numero de objetos
  objetos = []

  if x == 0 and y == 0 and n == 0:
    break

  for _ in range(n):
    objetos.append(int(input()))
  respostas.append(divisao_possivel(objetos,x+y))

for i, numero in enumerate(respostas):
  print(f"Teste {i+1}")
  print(numero)
  print()