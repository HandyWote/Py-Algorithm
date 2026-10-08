class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0
        while num1*num2 != 0:
            num1, num2 = min(num1, num2), abs(num1-num2)
            ans += 1
        return ans

def test():
    cases = {
        'input':[
            (2, 3),
            (10, 10)
        ],
        'output': [
            3,
            1
        ]
    }
    s = Solution()
    for i, c in enumerate(cases['input']):
        result = s.countOperations(*c)
        expected = cases['output'][i]
        assert result == expected, f"Test {i+1} failed, expected {expected} but get {result}"
        print(f"Test {i+1} passed")    
    print('All test passed')

if __name__ == "__main__":
    test()