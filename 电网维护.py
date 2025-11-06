from heapq import heapify, heappop


class Solution:
    def processQueries(self, c: int, connections: list[list[int]], queries: list[list[int]]) -> list[int]:
        g = [[] for _ in range(c + 1)]
        for x, y in connections:
            g[x].append(y)
            g[y].append(x)

        belong = [-1] * (c + 1)
        heaps = []

        def dfs(x: int) -> None:
            belong[x] = len(heaps)  # 记录节点 x 在哪个堆
            h.append(x)
            for y in g[x]:
                if belong[y] < 0:
                    dfs(y)

        for i in range(1, c + 1):
            if belong[i] >= 0:
                continue
            h = []
            dfs(i)
            heapify(h)
            heaps.append(h)

        ans = []
        offline = [False] * (c + 1)
        for op, x in queries:
            if op == 2:
                offline[x] = True
                continue
            if not offline[x]:
                ans.append(x)
                continue
            h = heaps[belong[x]]
            # 懒删除：取堆顶的时候，如果离线，才删除
            while h and offline[h[0]]:
                heappop(h)
            ans.append(h[0] if h else -1)
        return ans

def test():
    cases = {
        'input':[
            (5, [[1,2],[2,3],[3,4],[4,5]], [[1,3],[2,1],[1,1],[2,2],[1,2]]),
            (3, [], [[1,1],[2,1],[1,1]])
        ],
        'output': [
            [3,2,3],
            [1,-1]
        ]
    }
    s = Solution()
    for i, c in enumerate(cases['input']):
        result = s.processQueries(*c)
        expected = cases['output'][i]
        assert result == expected, f"Test {i+1} failed, expected {expected} but get {result}"
        print(f"Test {i+1} passed")    
    print('All test passed')

if __name__ == "__main__":
    test()