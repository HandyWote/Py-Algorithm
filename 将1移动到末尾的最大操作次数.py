class Solution:
    def maxOperations(self, s: str) -> int:
        ans = count1 = 0
        for i in range(len(s)):
            if s[i] == '1':
                count1 += 1
            elif i > 0 and s[i-1] == '1':
                ans += count1
        return ans

def test():
    cases = {
        'input':[
            "1001101",
            "00111"
        ],
        'output': [
            4,
            0
        ]
    }
    s = Solution()
    for i, c in enumerate(cases['input']):
        print(f"\n=== Test {i+1}: {c} ===")
        result = s.maxOperations(c)
        expected = cases['output'][i]
        print(f"Result: {result}, Expected: {expected}")
        assert result == expected, f"Test {i+1} failed, expected {expected} but get {result}"
        print(f"Test {i+1} passed")    
    print('All test passed')

if __name__ == "__main__":
    test()