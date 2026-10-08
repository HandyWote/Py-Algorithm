class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        m = 0
        start = 0
        temp = colors[0]
        for i in range(1, len(colors)):
            if colors[i] == temp:
                continue
            else:
                m += max(neededTime[start:i])
                start = i
                temp = colors[i]
        m += max(neededTime[start:]) 
        return sum(neededTime) - m
            


def test():
    cases = {
        'input':[
            ("abaac", [1,2,3,4,5]),
            ("abc", [1,2,3]),
            ("aabaa", [1,2,3,4,1]),
            ("bbbaaa", [4,9,3,8,8,9])
        ],
        'output': [
            3,
            0,
            2,
            23
        ]
    }
    s = Solution()
    for i, c in enumerate(cases['input']):
        result = s.minCost(*c)
        expected = cases['output'][i]
        assert result == expected, f"Test {i+1} failed, expected {expected} but get {result}"
        print(f"Test {i+1} passed")    
    print('All test passed')

if __name__ == "__main__":
    test()