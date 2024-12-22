# a soma dos numeros das casas eh igual a K
# nao existe outro par de casas cuja soma tenha esse mesmo valor

n = int(input())
casas = []
for _ in range(n):
  casas.append(int(input()))
k = int(input())

def alvo(casas,k,n):
  for i in range(n):
    for j in range(1,n):
      if casas[i] + casas[j] == k:
        return f"{str(casas[i])} {str(casas[j])}"
      
print(alvo(casas,k,n))