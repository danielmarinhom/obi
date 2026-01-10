#a quantidade de pares de esquinas que existe ao menos uma rua importante no caminho
#(A,B) e (B,A) sao o mesmo apr

n = int(input()) #esquinas
ruas = []
for _ in range(n-1):
  a,b,c = map(int,input().split())
  ruas.append((a,b,c))

def calc_e(ruas,n):
