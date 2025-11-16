class Solution:
    def numSub(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        s = s.split('0')
        for i in range(1, len(dp)):
            dp[i] = dp[i-1] + i
        ans = 0
        for sub in s:
            n = len(sub)
            ans += dp[n]
        return ans % (10**9 + 7)

def test():
    cases = {
        'input':[
            "0110111",
            "101",
            "111111"
            ],
        'output': [
            9,
            2,
            21
        ]
    }
    s = Solution()
    for i, c in enumerate(cases['input']):
        print(f"\n=== Test {i+1}: {c} ===")
        result = s.numSub(c)
        expected = cases['output'][i]
        print(f"Result: {result}, Expected: {expected}")
        assert result == expected, f"Test {i+1} failed, expected {expected} but get {result}"
        print(f"Test {i+1} passed")    
    print('All test passed')

if __name__ == "__main__":
    test()