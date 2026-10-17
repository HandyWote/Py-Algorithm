class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        sorted_nums: list[list[int]] = sorted([[sum(map(int, str(x))), x, i] for i, x in enumerate(nums)], key = lambda list: (list[0], list[1]))
        return self.count(sorted_nums)

    
    @staticmethod
    def count(sorted_nums: list[list[int]]) -> int:
        cnt: int = 0
        for _, _, index in sorted_nums:
            if index < 0:
                continue
            cnt += 1
            j: int = index
            while j >= 0:
                sorted_nums[j][2], j = -1, sorted_nums[j][2]
        return len(sorted_nums) - cnt

if __name__ == "__main__":
    s = Solution()
    print(s.minSwaps([18,43,34,16]))
    
