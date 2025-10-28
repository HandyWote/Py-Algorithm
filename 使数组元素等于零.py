class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        ans = 0
        for i, n in enumerate(nums):
            if n == 0:
                ans += self.beCalculate(nums, i)
        return ans
    
    def beCalculate(self, nums: list[int], index: int) -> int:
        if index+1>len(nums): return 0
        l, r = sum(nums[0:index]), sum(nums[index+1:])
        if l == r: return 2
        if abs(l-r) == 1: return 1
        return 0

def test():
    s = Solution()
    cases = {
        'input': [
            [1,0,2,0,3],
            [2,3,4,0,4,1,0],
            [16,13,10,0,0,0,10,6,7,8,7]
        ],
        'output':[
            2,
            0,
            3
        ]
    }
    for i, c in enumerate(cases['input']):
        assert s.countValidSelections(c) == cases['output'][i], f"Test {i+1} faild, expected {cases['output'][i]} but get {s.countValidSelections(c)}"
        print(f"Test {i+1} passed")
    print('All test passed')

if __name__ == '__main__':
    test()