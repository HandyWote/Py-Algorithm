from collections import Counter, deque
import heapq
class Solution:
    def __init__(self):
        self.heap = []
        self.window = []
        self.freq = {}
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        n = len(nums)
        ans = []
        self.temp = deque(nums[0:k])
        self.freq = Counter(list(self.temp))
        sorted_items = sorted(self.freq.items(), key=lambda item: (-item[1], -item[0]))
        len_sorted_items = len(sorted_items)
        result = 0
        for i in range(min(x, len_sorted_items)):
            result += sorted_items[i][0]*sorted_items[i][1]
        ans.append(result)
        for i in range(k, n):
            self.freq[self.temp.popleft()] -= 1
            self.freq[nums[i]] += 1
            self.temp.append(nums[i])
            sorted_items = sorted(self.freq.items(), key=lambda item: (-item[1], -item[0]))
            result = 0
            for i in range(min(x, len_sorted_items)):
                result += sorted_items[i][0]*sorted_items[i][1]
            ans.append(result)
        return ans

# from sortedcontainers import SortedList

# class Solution:
#     def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
#         cnt = defaultdict(int)
#         L = SortedList()  # 保存 tuple (出现次数，元素值)
#         R = SortedList()
#         sum_l = 0  # L 的元素和

#         def add(val: int) -> None:
#             if cnt[val] == 0:
#                 return
#             p = (cnt[val], val)
#             if L and p > L[0]:  # p 比 L 中最小的还大
#                 nonlocal sum_l
#                 sum_l += p[0] * p[1]
#                 L.add(p)
#             else:
#                 R.add(p)

#         def remove(val: int) -> None:
#             if cnt[val] == 0:
#                 return
#             p = (cnt[val], val)
#             if p in L:
#                 nonlocal sum_l
#                 sum_l -= p[0] * p[1]
#                 L.remove(p)
#             else:
#                 R.remove(p)

#         def l2r() -> None:
#             nonlocal sum_l
#             p = L[0]
#             sum_l -= p[0] * p[1]
#             L.remove(p)
#             R.add(p)

#         def r2l() -> None:
#             nonlocal sum_l
#             p = R[-1]
#             sum_l += p[0] * p[1]
#             R.remove(p)
#             L.add(p)

#         ans = [0] * (len(nums) - k + 1)
#         for r, in_ in enumerate(nums):
#             # 添加 in_
#             remove(in_)
#             cnt[in_] += 1
#             add(in_)

#             l = r + 1 - k
#             if l < 0:
#                 continue

#             # 维护大小
#             while R and len(L) < x:
#                 r2l()
#             while len(L) > x:
#                 l2r()
#             ans[l] = sum_l

#             # 移除 out
#             out = nums[l]
#             remove(out)
#             cnt[out] -= 1
#             add(out)
#         return ans


def test():
    cases = {
        'input':[
            ([1,1,2,2,3,4,2,3], 6, 2),
            ([3,8,7,8,7,5], 2, 2),
            ([1,4,4,4], 3, 2)
        ],
        'output': [
            [6,10,12],
            [11,15,15,15,12],
            [9, 12]
        ]
    }
    s = Solution()
    for i, c in enumerate(cases['input']):
        result = s.findXSum(*c)
        expected = cases['output'][i]
        assert result == expected, f"Test {i+1} failed, expected {expected} but get {result}"
        print(f"Test {i+1} passed")    
    print('All test passed')

if __name__ == "__main__":
    test()