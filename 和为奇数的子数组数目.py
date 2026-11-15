class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        ans: int = 0
        sums: list[int] = [0] * (len(arr)+1)
        cnt: list[int] = [0, 0]
        MOD: int = 1_000_000_007
        for i, x in enumerate(arr):
            sums[i + 1] = (sums[i] + x) % 2

        for i in sums:
            ans += cnt[i^1]
            cnt[i] += 1
        
        return ans%MOD

if __name__ == '__main__':
    s = Solution()
    print(s.numOfSubarrays([1,3,5]))
