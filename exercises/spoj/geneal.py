#grau(a,b) = 0, se a=b
#grau(a,b) = 1 + min{grau(pai(A), B), grau(A, pai(B))}, se A != B

n = int(input())
for _ in range(n):
  pai, filho = input().split()