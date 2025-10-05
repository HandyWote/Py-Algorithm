class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        pacific_reachable = [[False] * n for _ in range(m)]
        atlantic_reachable = [[False] * n for _ in range(m)]
        
        def dfs(i, j, reachable):
            reachable[i][j] = True
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if (0 <= ni < m and 0 <= nj < n and not reachable[ni][nj] and heights[ni][nj] >= heights[i][j]):
                    dfs(ni, nj, reachable)

        for i in range(m):
            dfs(i, 0, pacific_reachable)
        for j in range(n):
            dfs(0, j, pacific_reachable)
        for i in range(m):
            dfs(i, n - 1, atlantic_reachable)
        for j in range(n):
            dfs(m - 1, j, atlantic_reachable)

        result = []
        for i in range(m):
            for j in range(n):
                if pacific_reachable[i][j] and atlantic_reachable[i][j]:
                    result.append([i, j])
        
        return result

if __name__ == "__main__":
    solution = Solution()
    heights = [[1, 2, 2, 3, 5],
               [3, 2, 3, 4, 4],
               [2, 4, 5, 3, 1],
               [6, 7, 1, 4, 5],
               [5, 1, 1, 2, 4]]
    result = solution.pacificAtlantic(heights)
    print(result)  # 输出: [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]