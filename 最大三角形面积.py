from itertools import combinations


class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        ans = 0
        for p1, p2, p3 in combinations(points, 3):
            x1, y1 = p2[0] - p1[0], p2[1] - p1[1]
            x2, y2 = p3[0] - p1[0], p3[1] - p1[1]
            ans = max(ans, abs(x1 * y2 - y1 * x2))
        return ans / 2


if __name__ == "__main__":
    s = Solution()
    print(s.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))  # 2.0
