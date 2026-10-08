from math import gcd
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        if gcd(*nums) > 1:
            return -1
        min_size = n = len(nums)
        cout1 = sum(x == 1 for x in nums)
        if cout1: return n - cout1
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    min_size = min(min_size, j - i)
                    break
        return min_size + n - 1


def test():
    cases = {
        'input':[
            [2,6,3,4],
            [2,10,6,14],
            [410193,229980,600441],
            [6,10,15]
        ],
        'output': [
            4,
            -1,
            -1,
            4
        ]
    }
    s = Solution()
    for i, c in enumerate(cases['input']):
        print(f"\n=== Test {i+1}: {c} ===")
        result = s.minOperations(c)
        expected = cases['output'][i]
        print(f"Result: {result}, Expected: {expected}")
        assert result == expected, f"Test {i+1} failed, expected {expected} but get {result}"
        print(f"Test {i+1} passed")    
    print('All test passed')

if __name__ == "__main__":
    test()