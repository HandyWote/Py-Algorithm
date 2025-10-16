from collections import Counter



class Solution:
    def findSmallestInteger(self, nums: list[int], m: int) -> int:
        cnt = Counter(x % m for x in nums)
        mex = 0
        while cnt[mex % m]:
            cnt[mex % m] -= 1
            mex += 1
        return mex

def test():
    solution = Solution()
    # Add test cases here to validate the implementation
    assert solution.findSmallestInteger([1,-10,7,13,6,8], 5) == 4  # 4
    assert solution.findSmallestInteger([1,-10,7,13,6,8], 7) == 2  # 2
    print('All test cases passed!')

if __name__ == "__main__":
    test()