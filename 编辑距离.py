class Solution:
    def minDistance(self, s: str, t: str) -> int:
        f = list(range(len(t) + 1))
        for x in s:
            pre = f[0]
            f[0] += 1
            for j, y in enumerate(t):
                tmp = f[j + 1]
                f[j + 1] = pre if x == y else min(f[j + 1], f[j], pre) + 1
                pre = tmp
        return f[-1]


def test():
    s = Solution()
    cases = {
        'input': [
            ("horse", "ros"),
            ("intention", "execution")
        ],
        'output':[
            3,
            5
        ]
    }
    for i, c in enumerate(cases['input']):
        assert s.minDistance(c[0], c[1]) == cases['output'][i], f"Test {i+1} faild, expected {cases['output'][i]} but get {s.minDistance(c[0], c[1])}"
        print(f"Test {i+1} passed")
    print('All test passed')


if __name__ == '__main__':
    test()