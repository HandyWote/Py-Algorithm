import heapq
from collections import defaultdict

def get_date():
    m, n, q = map(int, input().split())
    roads = defaultdict(list)
    queries = []
    for _ in range(m):
        u, v, d = map(int, input().split())
        roads[u].append((v, d))
        roads[v].append((u, d))
    for _ in range(q):
        st, ed = map(int, input().split())
        queries.append((st, ed))
    return roads, queries, n

# Dijkstra算法求最短路径
def dijkstra(st, ed, roads):
    visited = set()
    heap = [(0, st)]  # (距离, 节点)
    while heap:
        dist, node = heapq.heappop(heap)
        if node in visited:
            continue
        if node == ed:
            return dist
        visited.add(node)
        for neighbor, d in roads[node]:
            if neighbor not in visited:
                heapq.heappush(heap, (dist + d, neighbor))
    return -1

if __name__ == '__main__':
    roads, queries, n = get_date()
    for st, ed in queries:
        min_d = dijkstra(st, ed, roads)
        print(min_d)
