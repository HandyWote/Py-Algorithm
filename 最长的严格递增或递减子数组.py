class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        ans: int = 0
        pos_cnt: int = 1
        neg_cnt: int = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                pos_cnt += 1
            else:
                ans = max(ans, pos_cnt)
                pos_cnt = 1

            if nums[i] > nums[i+1]:
                neg_cnt += 1
            else:
                ans = max(ans, neg_cnt)
                neg_cnt = 1
        return max(ans, pos_cnt, neg_cnt)
