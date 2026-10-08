from cmath import inf
from collections import defaultdict


class Solution:
    def countTrapezoids(self, points: list[list[int]]) -> int:
        cnt = defaultdict(lambda: defaultdict(int))  # 斜率 -> 截距 -> 个数
        cnt2 = defaultdict(lambda: defaultdict(int))  # 中点 -> 斜率 -> 个数

        for i, (x, y) in enumerate(points):
            for x2, y2 in points[:i]:
                dy = y - y2
                dx = x - x2
                k = dy / dx if dx else inf
                b = (y * dx - x * dy) / dx if dx else x
                cnt[k][b] += 1  # 按照斜率和截距分组
                cnt2[(x + x2, y + y2)][k] += 1  # 按照中点和斜率分组

        ans = 0
        for m in cnt.values():
            s = 0
            for c in m.values():
                ans += s * c
                s += c

        for m in cnt2.values():
            s = 0
            for c in m.values():
                ans -= s * c  # 平行四边形会统计两次，减去多统计的一次
                s += c

        return ans


if __name__ == "__main__":
    from test import Test

    cases = {
        'input': [
            [[-3,2],[3,0],[2,3],[3,2],[2,-3]],
            [[0,0],[1,0],[0,1],[2,1]],
        ],
        'output': [
            2,
            1,
        ]
    }

    test = Test(cases, Solution(), 'countTrapezoids')
    test.run()