class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        n = len(nums)
        while n:
            num = nums.pop(0)
            if num != val:
                nums.append(num)
                k += 1
            n -= 1
        return k
    # def removeElement(self, nums: List[int], val: int) -> int:
    #     i = 0
    #     for x in nums:
    #         if x != val:
    #             nums[i] = x
    #             i += 1
    #     return i
if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    ob = Solution()
    print(ob.removeElement(nums, val))