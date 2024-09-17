def bellman_ford_with_early_stopping(num_vertices, arestas, inicio):
    # Inicialização das distâncias
    dist = [float('inf')] * num_vertices
    dist[inicio] = 0

    for _ in range(num_vertices - 1):
        updated = False
        for u, num_vertices, w in arestas:
            if dist[u] != float('inf') and dist[u] + w < dist[num_vertices]:
                dist[num_vertices] = dist[u] + w
                updated = True
            if dist[num_vertices] != float('inf') and dist[num_vertices] + w < dist[u]:
                dist[u] = dist[num_vertices] + w
                updated = True

        if not updated:
            break

    for u, num_vertices, w in arestas:
        if dist[u] != float('inf') and dist[u] + w < dist[num_vertices]:
            return "Ciclo negativo detectado"

    # Formatação da saída
    return [d if d != float('inf') else "INF" for d in dist]