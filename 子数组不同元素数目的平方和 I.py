class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        n: int = len(nums)
        m: int = 0
        for i in range(n):
            st: set[int] = set()
            for j in range(i,n):
                st.add(nums[j])
                x: int = len(st)
                m += x**2
        return m
