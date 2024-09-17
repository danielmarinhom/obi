n,m = map(int,input().split()) #linhas e colunas
grafo = []
for _ in range(n):
    x = list(map(int,input().split()))
    grafo.append(x)

def bfs(grafo, n, m, x,y):
    novo = [[-1]*m for _ in range(m)]
    for i in range(n):
        for j in range(m):
            novo[i][j] = grafo[i][j]
    novo[x][y] = 0
    queue = [(x,y, grafo[x][y])]
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    while queue:
        x,y, poder = queue.pop(0)
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and novo[nx][ny] <= poder and novo[nx][ny] != 0 and poder != poder + novo[nx][ny]:
                novo[nx][ny] = 0
                queue.append((nx,ny, poder+novo[nx][ny]))
    return poder
resultados = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        resultados[i][j] = bfs(grafo, n, m, i,j)
for x in resultados:
    print(x)