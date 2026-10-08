class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        from collections import defaultdict
        d = defaultdict(int)
        ans = set()
        for i in nums:
            if i in ans: continue
            d[i] += 1
            if d[i] >= 2:
                ans.add(i)
        return list(ans)

def test():
    cases = {
        'input':[
            [0,1,1,0],
            [0,3,2,1,3,2],
            [7,1,5,4,3,4,6,0,9,5,8,2]
        ],
        'output': [
            [0, 1],
            [2, 3],
            [4, 5]
        ]
    }
    s = Solution()
    for i, c in enumerate(cases['input']):
        assert s.getSneakyNumbers(c) == cases['output'][i], f"Test {i+1} faild, expected {cases['output'][i]} but get {s.getSneakyNumbers(c)}"
        print(f"Test {i+1} passed")
    print('All test passed')

if __name__ == '__main__':
    test()