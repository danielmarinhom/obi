# LEITURA DAS COORDENADAS
n = int(input(""))
salas = []
for i in range(n):
    l = list(map(int, input("").split()))
    # Converte cada sala em um dicionário
    salas.append({'coords': l})

# Ordena as salas com base nas coordenadas
salas.sort(key=lambda x: (x['coords'][0], -x['coords'][2], -x['coords'][1], x['coords'][3]))

def contains(sala1, sala2):
    # Verifica se sala2 está contida em sala1
    x1, y1, x2, y2 = sala1['coords']
    a1, b1, a2, b2 = sala2['coords']
    return x1 <= a1 and y1 >= b1 and x2 >= a2 and y2 <= b2

def build_hierarchy(salas):
    hierarchy = []
    stack = []

    for sala in salas:
        # Remove da pilha enquanto a sala atual não estiver contida na sala no topo da pilha
        while stack and not contains(stack[-1], sala):
            stack.pop()

        # Se a pilha não estiver vazia, adiciona a sala atual como filha da sala no topo da pilha
        if stack:
            if 'children' not in stack[-1]:
                stack[-1]['children'] = []
            stack[-1]['children'].append(sala)
        else:
            # Se a pilha estiver vazia, adiciona a sala diretamente na hierarquia
            hierarchy.append(sala)

        # Adiciona a sala atual na pilha
        stack.append(sala)

    return hierarchy

def dfs(sala):
    if 'children' not in sala:
        return 1
    return sum(dfs(child) for child in sala['children'])

hierarchy = build_hierarchy(salas)
res = sum(dfs(sala) for sala in hierarchy)
print(res)
