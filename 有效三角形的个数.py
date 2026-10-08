class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                left, right = j + 1, n - 1
                k = j
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] < nums[i] + nums[j]:
                        k = mid
                        left = mid + 1
                    else:
                        right = mid - 1
                count += k - j
        return count

# class Solution:
#     def triangleNumber(self, nums: list[int]) -> int:
#         l = len(nums)
#         nums.sort()
#         ans = 0
#         for k in range(2, l):
#             c = nums[k]
#             i = 0
#             j = k - 1
#             while i < j:
#                 if nums[i] + nums[j] > c:
#                     ans += j - i
#                     j -= 1
#                 else:
#                     i += 1
#         return ans

if __name__ == "__main__":
    obj = Solution()
    print(obj.triangleNumber([0,1,1,1]))