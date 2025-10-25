class Solution:
    def distMoney(self, money: int, children: int) -> int:
        expected = children * 8
        if money > expected: return children-1
        elif money == expected: return children
        else:
            money -= children
            if money < 0: return -1
            ans = money//7
            res = money%7
            if res == 3 and children-ans == 1: return ans-1
            return ans

                

def test():
    s = Solution()
    cases = {
        'input': [
            (20, 3),
            (16, 2),
            (23, 3)
        ],
        'output': [
            1,
            2,
            2
        ]
    }
    for i, input in enumerate(cases['input']):
        output = cases['output'][i]
        assert s.distMoney(input[0], input[1]) == output, f"case {i+1} faild, expected {output} ,but get {s.distMoney(input[0], input[1])}"
        print(f"Test case {i+1} passed")

if __name__ == "__main__":
    test()