from bisect import bisect_right
from itertools import combinations, permutations


# class Solution:
#     def nextBeautifulNumber(self, n: int) -> int:
#         while True:
#             n += 1
#             if self.isBeautifulNumber(n):
#                 return n
#     def isBeautifulNumber(self, n: int) -> bool:
#         from collections import defaultdict
#         d = defaultdict(int)
#         for i in str(n):
#             d[int(i)] += 1
#         if all(d[i] == i for i in d):
#             return True
#         return False
    
t = [str(i) * i for i in range(1, 10)]
res = []
for i in range(1, len(t) + 1):
    for c in combinations(t, i):
        s = "".join(c)
        if len(s) > 8:
            continue
        for p in permutations(s):
            res.append(int("".join(p)))
res.sort()
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        return res[bisect_right(res, n)]
        

def test():
    s = Solution()
    cases = {
        'input': [
            1,
            1000,
            3000
        ],
        'output':[
            22,
            1333,
            3133
        ]
    }
    for i, input in enumerate(cases['input']):
        output = cases['output'][i]
        assert s.nextBeautifulNumber(input) == output, f"expected {output} ,but get {s.nextBeautifulNumber(input)}"
        print(f"Test case {i+1} passed")

if __name__ == '__main__':
    test()