from string import ascii_lowercase


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        for alpha in ascii_lowercase:  # 枚举两侧字母 alpha
            i = s.find(alpha)  # 最左边的 alpha 的下标
            if i < 0:  # s 中没有 alpha
                continue
            j = s.rfind(alpha)  # 最右边的 alpha 的下标
            ans += len(set(s[i + 1: j]))  # 统计有多少个不同的中间字母
        return ans


if __name__ == "__main__":
    from test import Test
    cases = {
        'input':["aabca",
                 "adc", 
                 "bbcbaba"],
        'output': [3,
                   0,
                   4]}
    test = Test()
    test.run()