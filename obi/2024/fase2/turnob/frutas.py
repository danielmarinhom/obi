r, n = map(int,input().split()) # reais, n de frutas
frutas = []
for _ in range(n):
    t, p = map(int,input().strip().split()) # tipo, preco (tipo entre 1 e 100)
    frutas.append((t,p))

frutas.sort(key = lambda x: x[1])
usados = set()
for i in range(len(frutas)):
    t, p = frutas[i]
    if t not in usados and r-p >= 0:
        r -= p
        usados.add(t)
print(len(usados))