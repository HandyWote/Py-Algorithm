class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            t: str = ''
            for i in range(0, len(s), k):
                num: int = sum(map(int, s[i: i+k]))
                t += str(num)
            s = t
        return s
