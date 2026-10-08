from collections import defaultdict


class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        d = defaultdict(list)
        ans = 0
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                d[i].append(strs[j][i])
    
        for i in d:
            if d[i] == sorted(d[i]):
                continue
            ans += 1
        return ans

if __name__ == '__main__':
    from test import Case, Test
    cases = Case(
        [
            (["cba","daf","ghi"], 1),
            (["a","b"], 0),
            (["zyx","wvu","tsr"], 3)
        ]
    )
    Test(cases, Solution(), 'minDeletionSize').run()