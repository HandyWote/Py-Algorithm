class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        result = 0
        while n > 0:
            result ^= n
            n >>= 1
        return result


def test():
    cases = {
        'input':[
            3,
            6
        ],
        'output': [
            2,
            4
        ]
    }
    s = Solution()
    for i, c in enumerate(cases['input']):
        result = s.minimumOneBitOperations(c)
        expected = cases['output'][i]
        assert result == expected, f"Test {i+1} failed, expected {expected} but get {result}"
        print(f"Test {i+1} passed")    
    print('All test passed')

if __name__ == "__main__":
    test()