class Solution:
    def specialTriplets(self, nums: list[int]) -> int:
        MOD = 1000000007
        n = len(nums)

        from collections import Counter
        total = Counter(nums)
        prefix = Counter()

        ans = 0
        for j in range(n):
            target = nums[j] * 2
            count_i = prefix[target]
            count_k = total[target] - prefix[target]
            if nums[j] == target:
                count_k -= 1

            ans += count_i * count_k
            ans %= MOD

            prefix[nums[j]] += 1

        return ans
    

if __name__ == "__main__":
    from test import Case, Test
    cases = Case()
    cases.add_cases(
        (
            ([6,3,6], 1),
            ([0,1,0,0], 1),
            ([8,4,2,8,4], 2),
            ([56,56,87,28,55,56,94], 2)
        )
    )
    Test(cases, Solution(), 'specialTriplets').run()