from functools import cache


class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        cnt0 = [s.count('0') for s in strs]

        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, j: int, k: int) -> int:
            if i < 0:
                return 0
            res = dfs(i - 1, j, k)  # 不选 strs[i]
            cnt1 = len(strs[i]) - cnt0[i]
            if j >= cnt0[i] and k >= cnt1:
                res = max(res, dfs(i - 1, j - cnt0[i], k - cnt1) + 1)  # 选 strs[i]
            return res

        return dfs(len(strs) - 1, m, n)

def test():
    cases = {
        'input':[
            (["10", "0001", "111001", "1", "0"], 5, 3),
            (["10", "0", "1"], 1, 1)
        ],
        'output': [
            4,
            2
        ]
    }
    s = Solution()
    for i, c in enumerate(cases['input']):
        print(f"\n=== Test {i+1}: {c} ===")
        result = s.findMaxForm(*c)
        expected = cases['output'][i]
        print(f"Result: {result}, Expected: {expected}")
        assert result == expected, f"Test {i+1} failed, expected {expected} but get {result}"
        print(f"Test {i+1} passed")    
    print('All test passed')

if __name__ == "__main__":
    test()