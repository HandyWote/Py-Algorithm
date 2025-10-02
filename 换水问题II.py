from math import isqrt


class Solution:
    def maxBottlesDrunk(self, n: int, e: int) -> int:
        b = e * 2 - 1
        k = (isqrt(b * b + (n - e) * 8) - b + 2) // 2
        return n + k
