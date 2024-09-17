#n alunos, nota que mais aparece
#se houver mais de uma, a maior

n = int(input())
notas = list(map(int,input().split()))

vezes = 0
res = 0
for nota in notas:
  if notas.count(nota) >= vezes and nota > res:
    vezes = notas.count(nota)
    res = nota  
print(res)

#3 min e 30 
