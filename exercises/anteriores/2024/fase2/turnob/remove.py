n = int(input())

def getMaior(n):
    nstr = str(n)
    maior = int(nstr[0])
    for x in nstr:
        if int(x) > maior:
            maior = int(x)
    return maior

def remove(n):
    steps = 0
    while n != 0:
        maior = getMaior(n)
        n -= maior
        steps += 1
    return steps
print(remove(n))
