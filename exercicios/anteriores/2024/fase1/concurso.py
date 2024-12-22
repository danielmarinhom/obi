n, k = input("").strip().split()
n, k = int(n), int(k)
notas = input("").strip().split()

notas = list(map(int, notas)) #converte pra int
notas.sort()

temp = notas[-k:]
corte = temp[0]
print(corte)

