class Solution:
    def countCoveredBuildings(self, n: int, buildings: list[list[int]]) -> int:
        row_min = [n + 1] * (n + 1)
        row_max = [0] * (n + 1)
        col_min = [n + 1] * (n + 1)
        col_max = [0] * (n + 1)

        for x, y in buildings:
            # 手写 min max 更快
            if x < row_min[y]: row_min[y] = x
            if x > row_max[y]: row_max[y] = x
            if y < col_min[x]: col_min[x] = y
            if y > col_max[x]: col_max[x] = y

        ans = 0
        for x, y in buildings:
            if row_min[y] < x < row_max[y] and col_min[x] < y < col_max[x]:
                ans += 1
        return ans


if __name__ == '__main__':
    from test import Case, Test
    cases = Case()
    cases.add_cases(
        (
            ((3, [[1,2],[2,2],[3,2],[2,1],[2,3]]), 1),
            ((3, [[1,1],[1,2],[2,1],[2,2]]), 0),
            ((5, [[1,3],[3,2],[3,3],[3,5],[5,3]]), 1)
        )
    )
    Test(cases, Solution(), 'countCoveredBuildings').run()