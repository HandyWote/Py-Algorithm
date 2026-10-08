class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start: int):
            if start == len(nums) - 1:
                res.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        res = []
        backtrack(0)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.permute([1,2,3]))  # Example test case