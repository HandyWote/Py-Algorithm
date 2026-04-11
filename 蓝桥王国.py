def get_data():
    n, m = map(int, input().split())
    dist = [[] for _ in range(n+1)]
    grid = [[float('inf')] * n for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        grid[u-1][v-1] = w
        dist[u-1].append((v-1, w))

    for i in range(n):
        grid[i][i] = 0

    return n,grid, dist

def floyd(n, grid):
    for k in range(n):
        for i in range(n):
            if grid[i][k] == float('inf'):
                continue
            for j in range(n):
                if grid[k][j] == float('inf'):
                    continue
                if grid[i][j] > grid[i][k] + grid[k][j]:
                    grid[i][j] = grid[i][k] + grid[k][j]
    return grid

def dijkstra(n, dist):
    import heapq
    d = [float('inf')] * n
    d[0] = 0
    q = [(0, 0)]
    while q:
        dis, u = heapq.heappop(q)
        if dis > d[u]:
            continue
        for v, w in dist[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                heapq.heappush(q, (d[v], v))
    return d

if __name__ == "__main__":
    n, grid, dist = get_data()
    d = dijkstra(n, dist)
    for i in range(n):
        print(-1 if d[i] == float('inf') else d[i], end=" ")