class Solution:
    def maxSelectedElements(self, nums: list[int]) -> int:
        nums.sort()
        from collections import defaultdict
        d: defaultdict[int, int] = defaultdict(int)
        for i in nums:
            d[i+1] = d[i] + 1
            d[i] = d[i-1] + 1
        return max(d.values())

if __name__ == "__main__":
    s = Solution()
    print(s.maxSelectedElements([2,1,5,1,1]))
