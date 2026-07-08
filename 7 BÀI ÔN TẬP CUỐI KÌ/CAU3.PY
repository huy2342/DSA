INF = 9999

graph = [
    [0, 2,5],
    [INF,0, INF],
    [INF, -4, 0]
]
dist = [0, INF, INF]
visited =[False, False, False]

n = 3

for i in range(n):
    u = -1
    for j in range(n):
        if not visited[j] and (u== -1 or dist[j] < dist[u]):
            u = j

    visited[u] = True

    for v in range(n):
        if graph[u][v] !=INF:
            if dist[u] + graph[u][v]< dist[v]:
                dist[v] = dist[u] + graph[u][v]
print(dist)