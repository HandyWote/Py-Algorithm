class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0
    
if __name__ == "__main__":
    s = Solution()
    print(s.largestPerimeter([2,1,2]))  # Output: 5
    print(s.largestPerimeter([1,2,1,10]))  # Output: 0
