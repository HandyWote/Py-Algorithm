class Solution:
    def smallestNumber(self, n: int) -> int:
        c = list(format(n, 'b'))
        n = len(c)
        for i in range(n):
            if c[i] != '1':
                c[i] = '1'
        c = ''.join(c)
        return int(c, 2)

def test():
    s = Solution()
    cases = {
        'input': [
            5,
            10,
            3
        ],
        'output':[
            7,
            15,
            3
        ]
    }
    for i, c in enumerate(cases['input']):
        assert s.smallestNumber(c) == cases['output'][i], f"Test {i+1} faild, expected {cases['output'][i]} but get {s.smallestNumber(c)}"
        print(f"Test {i+1} passed")
    print('All test passed')

if __name__ == '__main__':
    test()