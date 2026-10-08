from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        freq = Counter(nums)
        max_freq = max(freq.values())
        total_freq = sum(count for count in freq.values() if count == max_freq)
        return total_freq

if __name__ == "__main__":
    obj = Solution()
    print(obj.maxFrequencyElements([1,2,2,3,1,4]))  # 4
    print(obj.maxFrequencyElements([1,2,3,4,5]))    # 5