#usado para calcular as menores distancias entre todos os PARES de vertices em um grafo PONDERADO
#aceita pesos POSITIVOS e NEGATIVOS mas SEM ciclos negativos

n = int(input)
m = int(input)
matriz = [[-1] * n for _ in range(n)]
for _ in range(m):
  u,v,t = map(int,input().split())
  matriz[u-1][v-1] = t
  
def floyd_warshall(matriz):
    # Número de vértices no grafo
    V = len(matriz)
    
    # Inicializando a matriz de distâncias com os valores do grafo
    dist = [[float('inf')] * V for _ in range(V)]
    for i in range(V):
        for j in range(V):
            if i == j:
                dist[i][j] = 0
            elif matriz[i][j] != -1:
                dist[i][j] = matriz[i][j]

    # Atualizando a matriz de distâncias
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    #OPCIONAL: atualizar a matriz original com os resultados
    for i in range(V):
      for j in range(V):
        if dist[i][j] == float('inf'):
            matriz[i][j] = -1
        else:
            matriz[i][j] = dist[i][j]

    return dist