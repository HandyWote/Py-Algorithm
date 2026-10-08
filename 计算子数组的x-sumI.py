class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        n = len(nums)
        ans = []
        for i in range(n-k+1):
            temp = nums[i:i+k]
            if x >= k:
                ans.append(sum(temp))
            else:
                ans.append(self.findNums(temp, x))
        return ans

    def findNums(self, temp: list[int], x: int) -> int:
        from collections import Counter
        freq = Counter(temp)
        sorted_items = sorted(freq.items(), key=lambda item: (-item[1], -item[0]))
        result = 0
        for i in range(min(x, len(sorted_items))):
            result += sorted_items[i][0]*sorted_items[i][1]
        return result


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