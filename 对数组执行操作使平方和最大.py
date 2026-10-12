class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD: int = 10**9 + 7
        cnt1: list[int] = [0]*31 # 10**9 < 2**31
        ans: int = 0
        for num in nums:
            for i in range(31):
                if (num >> i) & 1:
                    cnt1[i] += 1

        for i in range(k):
            v: int = 0
            for j in range(31):
                if cnt1[j] > i:
                    v |= (1 << j)
            ans = (ans + v**2) % MOD
        
        return ans

