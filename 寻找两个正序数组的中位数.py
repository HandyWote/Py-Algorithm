import heapq
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        n: int = (len(nums1) + len(nums2))
        nums: list[int] = list(heapq.merge(nums1, nums2))
        if n%2 == 0:
            return (nums[n//2 - 1] + nums[n//2]) / 2
        return nums[n//2]