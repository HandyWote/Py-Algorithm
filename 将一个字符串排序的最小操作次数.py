class Solution:
    def minOperations(self, s: str) -> int:
        if all(x <= y for x, y in pairwise(s)):
            return 0

        if len(s) == 2:
            return -1
        
        mn: str = min(s)
        mx: str = max(s)

        if s[0] == mn or s[-1] == mx:
            return 1

        if any(x == mx or x == mn for x in s[1:-1]):
            return 2

        return 3
