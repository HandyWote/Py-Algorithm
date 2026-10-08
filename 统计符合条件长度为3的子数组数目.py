class Solution:
    def check(self, a: int, b: int, c: int) -> bool:
        if 2*(a+c) == b:
            return True
        return False
    
    def countSubarrays(self, nums: list[int]) -> int:
        ans = 0
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i+1], nums[i+2]
            if self.check(a, b, c):
                ans += 1
        return ans

if __name__ == "__main__":
    obj = Solution()
    print(obj.countSubarrays([1,2,1,4,1]))
    print(obj.countSubarrays([1,1,1]))
