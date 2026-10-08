# class Solution:
#     def canJump(self, nums: list[int]) -> bool:
#         dp = [False] * len(nums)
#         dp[-1] = True
#         for i in range(len(nums) - 2, -1, -1):
#             for j in range(1, nums[i] + 1):
#                 if i + j < len(nums) and dp[i + j]:
#                     dp[i] = True
#                     break
#         return dp[0]
    
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)-1
        last_need = 1
        for i in range(n-1,-1,-1):
            if nums[i] < last_need:
                last_need += 1
            else:
                last_need = 1
        if last_need == 1:
            return True
        return False

def test():
    solution = Solution()
    assert solution.canJump([2, 3, 1, 1, 4]) == True, "Test case 1 failed"
    assert solution.canJump([3, 2, 1, 0, 4]) == False, "Test case 2 failed"
    assert solution.canJump([0]) == True, "Test case 3 failed"
    assert solution.canJump([1, 0]) == True, "Test case 4 failed"
    assert solution.canJump([2, 0, 0]) == True, "Test case 5 failed"
    assert solution.canJump([1, 2, 3]) == True, "Test case 6 failed"
    assert solution.canJump([2, 5, 0, 0]) == True, "Test case 7 failed"
    print("All test cases passed!")

if __name__ == "__main__":
    test()
