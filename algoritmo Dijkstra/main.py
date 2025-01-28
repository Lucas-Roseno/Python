import numpy as np

grafo = np.array([[0, 10, 0, 30, 100], 
                  [10, 0, 50, 0, 0], 
                  [0, 50, 0, 20, 10], 
                  [30, 0, 20, 0, 60], 
                  [100, 0, 10, 60, 0]])

def dijkstra(grafo, start):
    n = len(grafo)
    dist = [float('inf')] * n
    dist[start] = 0
    visited = [False] * n

    for _ in range(n):
        min_dist = float('inf')
        min_index = -1
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                min_index = i

        visited[min_index] = True

        for j in range(n):
            if grafo[min_index][j] > 0 and not visited[j]:
                new_dist = dist[min_index] + grafo[min_index][j]
                if new_dist < dist[j]:
                    dist[j] = new_dist

    return dist

start_node = 0
distances = dijkstra(grafo, start_node)
print(f"Distâncias do nó {start_node} para todos os outros nós: {distances}")