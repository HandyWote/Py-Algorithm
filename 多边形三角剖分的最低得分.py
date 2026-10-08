from functools import cache


class Solution:
    def minScoreTriangulation(self, v: list[int]) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            if i + 1 == j:
                return 0
            return min(dfs(i, k) + dfs(k, j) + v[i] * v[j] * v[k] for k in range(i + 1, j))

        return dfs(0, len(v) - 1)


if __name__ == "__main__":
    s = Solution()
    print(s.minScoreTriangulation([1, 2, 3]))  # Output: 6
    print(s.minScoreTriangulation([3, 7, 4, 5]))  # Output: 144
    print(s.minScoreTriangulation([1, 3, 1, 4, 1, 5]))  # Output: 13