class Solution:
    def maxSumOfSquares(self, n: int, sum: int) -> str:
        if n * 9 < sum:
            return ""
        times, rem = divmod(sum, 9)
        ans: str = '9' * times
        if rem:
            ans += str(rem)
        return ans + '0' * (n - len(ans))

