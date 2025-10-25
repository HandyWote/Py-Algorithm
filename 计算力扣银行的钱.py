class Solution:
    def csum(self, n: int, i: int = 7) -> int:
        return i*(2*n+i-1)//2

    def totalMoney(self, n: int) -> int:
        a = n // 7
        ans = 0
        for i in range(1, a+1):
            ans += self.csum(i)
        return ans + self.csum(1+a, n%7)

    
    

def test():
    s = Solution()
    cases = {
        'input': [
            4,
            10,
            20
        ],
        'output': [
            10,
            37,
            96
        ]
    }
    for i, input in enumerate(cases['input']):
        output = cases['output'][i]
        assert s.totalMoney(input) == output, f"expected {output} ,but get {s.totalMoney(input)}"
        print(f"Test case {i+1} passed")

if __name__ == "__main__":
    test()