from collections import defaultdict
import heapq

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        adj = self.build(edges)
        return self.dijkstra(n, adj, labels, k)
    
    @staticmethod
    def build(edges: list[list[int]]) -> defaultdict[int, list[list[int]]]:
        adj: defaultdict[int, list[list[int]]] = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1:])
        return adj
    
    @staticmethod
    def check(u: int, v: int, c: int, labels: str, k: int) -> int:
        if labels[u] == labels[v]:
            c += 1
        else:
            c = 1
        return c if c <= k else -1

    @staticmethod
    def dijkstra(n: int, adj: defaultdict[int, list[list[int]]], labels: str, k: int) -> int:
        if n == 1:
            return 0
            
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        que = [(0, 0, 1)]

        while que:
            d, u, c = heapq.heappop(que)
            if d > dist[u][c]:
                continue
            if u == n - 1:
                return d
            for neighbor, weight in adj[u]:
                new_c = Solution.check(u, neighbor, c, labels, k)
                if new_c == -1:
                    continue
                nd = d + weight
                if nd < dist[neighbor][new_c]:
                    dist[neighbor][new_c] = nd
                    heapq.heappush(que, (nd, neighbor, new_c))

        return -1
