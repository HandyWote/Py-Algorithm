from sortedcontainers import SortedList


class Solution:
    def avoidFlood(self, rains: list[int]) -> list[int]:
        n = len(rains)
        ans = [-1] * n
        full_day = {}
        dry_day = SortedList()
        for i, lake in enumerate(rains):
            if lake == 0:
                ans[i] = 1
                dry_day.add(i)
                continue
            if lake in full_day:
                j = full_day[lake]
                k = dry_day.bisect_right(j)
                if k == len(dry_day):
                    return []
                d = dry_day[k]
                ans[d] = lake
                dry_day.discard(d)
            full_day[lake] = i
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.avoidFlood([1,2,3,4]))