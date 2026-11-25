
# class Solution:
#     def smallestUniqueSubarray(self, nums: list[int]) -> int:
#         from collections import Counter
#         c: Counter = Counter(get_sub(nums))
#         ans: int = min(len(k) for k, v in c.items() if v == 1)
#         return ans

# def get_sub(arr: list[int]):
#     n: int = len(arr)
#     for i in range(n):
#         for j in range(i + 1, n + 1):
#             yield tuple(arr[i: j])

class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        from collections import defaultdict
        n: int = len(nums)
        for length in range(1, n + 1):
            d: defaultdict[tuple[int], int] = defaultdict(int)
            for i in range(n - length + 1):
                d[tuple(nums[i: i+length])] += 1
            if any(i == 1 for i in d.values()):
                return length
        return -1

# class Solution:
#     def smallestUniqueSubarray(self, nums: list[int]) -> int:
#         n = len(nums)
#         # 多项式哈希（方便计算子数组哈希值）
#         # 哈希函数 hash(nums) = nums[0] * base^(n-1) + nums[1] * base^(n-2) + ... + nums[n-2] * base + nums[n-1]
#         MOD = 1_070_777_777
#         BASE = randint(8 * 10 ** 8, 9 * 10 ** 8)  # 随机 BASE，防止 hack
#         pow_base = [1] + [0] * n  # pow_base[i] = BASE^i
#         pre_hash = [0] * (n + 1)  # 前缀哈希值 pre_hash[i] = hash(nums[:i])
#         for i, x in enumerate(nums):
#             pow_base[i + 1] = pow_base[i] * BASE % MOD
#             pre_hash[i + 1] = (pre_hash[i] * BASE + x) % MOD  # 秦九韶算法计算多项式哈希

#         # 计算子数组 nums[l:r] 的哈希值，注意这是左闭右开区间 [l,r)
#         # 计算方法类似前缀和
#         def sub_hash(l: int, r: int) -> int:
#             return (pre_hash[r] - pre_hash[l] * pow_base[r - l]) % MOD

#         def check(length: int) -> bool:
#             cnt = defaultdict(int)
#             for i in range(length, n + 1):
#                 h = sub_hash(i - length, i)
#                 cnt[h] += 1
#             return 1 in cnt.values()

#         return bisect_left(range(n), True, lo=1, key=check)


if __name__ == '__main__':
    s = Solution()
    print(s.smallestUniqueSubarray([2,1,2,3,3]))
    print(s.smallestUniqueSubarray([19154,77544,19154]))
