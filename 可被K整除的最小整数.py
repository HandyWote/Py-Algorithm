class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        seen = set()
        x = 1 % k
        while x and x not in seen:
            seen.add(x)
            x = (x * 10 + 1) % k
        return -1 if x else len(seen) + 1


if __name__ == '__main__':
    cases = {
        'input':[
            1,
            2,
            3
        ],
        'output':[
            1,
            -1,
            3
        ]
    }
    from test import Test
    Test(cases, Solution(), 'smallestRepunitDivByK').run()