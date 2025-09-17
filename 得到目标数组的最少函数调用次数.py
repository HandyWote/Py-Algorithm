class Solution:
    def minOperations(self, nums: list[int]) -> int:
        ans = 0
        if nums == [0]: return 0
        while nums != [0]*len(nums):
            for i, n in enumerate(nums):
                if n % 2 == 0:
                    continue
                else:
                    nums[i] -= 1
                    ans += 1
            nums = [i/2 for i in nums]
            ans += 1
        return ans-1

if __name__ == '__main__':
    nums = [4,2,5]
    nums = [1,5]
    obj = Solution()
    print(obj.minOperations(nums))