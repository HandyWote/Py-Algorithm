class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        ans: float = float('inf')
        for left in range(len(nums)):
            cnt: int = 0
            for right in range(left, min(len(nums), left+r)):
                cnt += nums[right]
                lenth = right-left+1
                if lenth >= l and cnt > 0:
                    ans = min(ans, cnt)
        return -1 if ans == float('inf') else int(ans)

