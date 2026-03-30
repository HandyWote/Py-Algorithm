from test import Test, Case


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        from collections import Counter
        return Counter(s1[::2]) == Counter(s2[::2]) and Counter(s1[1::2]) == Counter(s2[1::2])

if __name__ == "__main__":
    cases = Case([
        (("abcdba", "cabdab"), True)
        ])
    solution = Solution()
    Test(cases, solution, "checkStrings").run()