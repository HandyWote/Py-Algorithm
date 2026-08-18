class Solution:
    def trap(self, height: List[int]) -> int:
        l = [0] * len(height)
        r = [0] * len(height)
        for i, h in enumerate(height):
            l[i] = max(l[i-1], h)
        for i, h in enumerate(height[::-1]):
            r[i] = max(r[i-1], h)
        r = r[::-1]
        res = 0
        for i, h in enumerate(height):
            res += min(l[i], r[i]) - h
        return res