class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        ans = set()
        def backtrack(start: int):
            if start == len(nums) - 1:
                ans.add(tuple(nums[:]))
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        backtrack(0)
        return [list(t) for t in ans]

if __name__ == "__main__":
    s = Solution()
    print(s.permuteUnique([1, 1, 2]))
    print(s.permuteUnique([1, 2, 3]))