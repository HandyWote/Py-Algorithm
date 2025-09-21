class Solution:
    def sumDigitDifferences(self, nums: list[int]) -> int:
        res = 0
        n = len(nums)
        while nums[0] > 0:
            cnt = [0] * 10
            for i in range(n):
                cnt[nums[i] % 10] += 1
                nums[i] = nums[i] // 10
            for i in range(10):
                res += (n - cnt[i]) * cnt[i]
        return res // 2

if __name__ == "__main__":
    s = Solution()
    print(s.sumDigitDifferences([13,23,12]))