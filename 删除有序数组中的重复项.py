class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        c = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[c] = nums[i]
                c += 1
        return c
if __name__ == "__main__":
    nums =[0,0,1,1,1,2,2,3,3,4] #[1,1,2] 
    ob = Solution()
    print(ob.removeDuplicates(nums))