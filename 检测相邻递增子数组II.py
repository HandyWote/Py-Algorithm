class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        ans = pre_cnt = cnt = 0
        for i, x in enumerate(nums):
            cnt += 1
            if i == len(nums) - 1 or x >= nums[i + 1]:
                ans = max(ans, cnt // 2, min(pre_cnt, cnt))
                pre_cnt = cnt
                cnt = 0
        return ans

    
def test():
    assert Solution().maxIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1]) == 3, str(Solution().maxIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1]))
    assert Solution().maxIncreasingSubarrays([1,2,3,4,4,4,4,5,6,7]) == 2, str(Solution().maxIncreasingSubarrays([1,2,3,4,4,4,4,5,6,7]))
    print("All tests passed.")

if __name__ == "__main__":
    test()