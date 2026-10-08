from collections import deque


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        d = deque()
        max_sum = float('-inf')
        current_sum = 0
        for num in nums:
            current_sum += num
            d.append(num)
            max_sum = max(max_sum, current_sum)
            while current_sum < 0 and d:
                removed = d.popleft()
                current_sum -= removed
        return max_sum

if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Expected output: 6
    print(s.maxSubArray([1]))  # Expected output: 1
    print(s.maxSubArray([5,4,-1,7,8]))  # Expected output: 23