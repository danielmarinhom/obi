n,m = map(int,input().split()) #linhas e colunas
grafo = []
for _ in range(n):
    x = list(map(int,input().split()))
    grafo.append(x)

def bfs(grafo:list, n, m, x,y):
    v = [[-1]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            v[i][j] = grafo[i][j]
            
    directions = [(0,1),(0,-1),(1,0),(-1,0)] #nslo
    queue = [(x,y, grafo[x][y])]
    v[x][y] = 0
    while queue:
        x, y, poder = queue.pop(0)
        #print(poder)
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and v[nx][ny] <= poder and poder != poder + v[nx][ny]:
                queue.append((nx,ny, poder + v[nx][ny]))
                v[nx][ny] = 0
    return poder
resultados = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        resultados[i][j] = bfs(grafo, n, m, i,j)
print(resultados)