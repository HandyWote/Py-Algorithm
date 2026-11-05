class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        ans: int = 0
        for i in arr1:
            if all(abs(i - j) > d for j in arr2):
                ans += 1
        return ans
