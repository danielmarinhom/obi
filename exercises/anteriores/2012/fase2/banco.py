# atendimento max 20
# quantos clientes esperarao mais de 20 min

c, n = map(int,input().split()) # numero de caixas, numero de clientes
clientes = []
for _ in range(n):
  t,d = map(int,input().split()) # momento em minutos que o cliente entrou, tempo necessario
  clientes.append((t,d))


def clientes_fudidos(c,n,clientes):
  res = 0
  for i in range(c):
    tempo_atual = 0
    for t,d in clientes:
      tempo_atual -= t
      if tempo_atual - t >= 20:
        res += 1
      tempo_atual += d

  return res

print(clientes_fudidos(c,n,clientes))