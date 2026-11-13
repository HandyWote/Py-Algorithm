from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        ans: int = 0
        window: deque[int] = deque() 
        cost: int = 0
        right: int = len(nums) - 1
        
        for left in range(len(nums) - 1, -1, -1):
            while window and nums[window[-1]] < nums[left]:
                idx = window.pop()
                next_greater_idx = window[-1] if window else right + 1
                cost += (nums[left] - nums[idx]) * (next_greater_idx - idx)
            
            window.append(left)
            
            while cost > k:
                if window[0] == right:
                    _ = window.popleft()
                else:
                    cost -= nums[window[0]] - nums[right]
                right -= 1
                
            ans += right - left + 1
            
        return ans
