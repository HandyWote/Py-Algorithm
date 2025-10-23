class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = list(map(int, s))
        while len(s)>2:
            s = [(s[i]+s[i+1])%10 for i in range(len(s)-1)]
        return s[0] == s[1]

def test():
    solution = Solution()
    cases = {
        'input': [
            "3902",
            "34789",
            "323"
        ],
        'output': [
            True,
            False,
            True
        ]   
    }
    for i, input in enumerate(cases['input']):
        output = cases['output'][i]
        assert solution.hasSameDigits(input) == output
        print(f"Test case {i+1} passed")

if __name__ == "__main__":
    test()