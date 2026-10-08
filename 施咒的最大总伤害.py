from collections import Counter
from functools import cache


class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        cnt = Counter(power)
        a = sorted(cnt)

        @cache
        def dfs(i: int) -> int:
            if i < 0:
                return 0
            x = a[i]
            j = i
            while j and a[j - 1] >= x - 2:
                j -= 1
            return max(dfs(i - 1), dfs(j - 1) + x * cnt[x])

        return dfs(len(a) - 1)

if __name__ == "__main__":
    obj = Solution()
    print(obj.maximumTotalDamage([1,1,3,4]))
    print(obj.maximumTotalDamage([7,1,6,6]))
    print(obj.maximumTotalDamage([5,9,2,10,2,7,10,9,3,8]))