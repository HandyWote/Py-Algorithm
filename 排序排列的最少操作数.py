class Solution:
    def minOperations(self, nums: list[int]) -> int:
        a, d = self.asc(nums), self.dasc(nums)
        ans = [x for x in (a, d) if x >= 0]
        return min(ans) if ans else -1

    @staticmethod
    def asc(nums: list[int]) -> int:
        n = len(nums)
        k: int = -1
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                if k != -1:
                    return -1
                k = i

        if k == -1:
            return 0
        return min(k, n - k + 2) if nums[0] >= nums[-1] else -1

    @staticmethod
    def dasc(nums: list[int]) -> int:
        n = len(nums)
        k: int = -1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                if k != -1:
                    return -1
                k = i

        if k == -1:
            return 1

        return min(k, n - k) + 1 if nums[0] <= nums[-1] else -1


