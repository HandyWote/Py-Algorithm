from collections import defaultdict
from pprint import pprint


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: list[list[int]], values: list[int], k: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node: int, parent: int) -> int:
            nonlocal ans
            s = values[node]
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                s += dfs(neighbor, node)
            ans += s % k == 0
            return s

        ans = 0
        dfs(0, -1)
        return ans


if __name__ == "__main__":
    cases = {
        'input': [
            (5, [[0,2],[1,2],[1,3],[2,4]], [1,8,1,4,4], 6),
            (7, [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], [3,0,6,1,5,2,1], 3),
        ],
        'output': [
            2,
            3,
        ]
    }
    from test import Test
    Test(cases, Solution(), 'maxKDivisibleComponents').run()