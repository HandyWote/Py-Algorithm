class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        cnt, precnt, ans = 1, 0, 0
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                cnt += 1
            else:
                precnt, cnt = cnt, 1
            ans = max(ans, min(precnt, cnt))
            ans = max(ans, cnt // 2)
        return ans >= k

                
if __name__ == "__main__":
    s = Solution()
    print(s.hasIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1], 3)) # True