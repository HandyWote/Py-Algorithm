from math import isqrt


class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for a in range(1, n):
            for b in range(1, a):
                if a * a + b * b > n * n:
                    break
                c2 = a * a + b * b
                if isqrt(c2) ** 2 == c2:
                    ans += 1
        return ans * 2


if __name__ == '__main__':
    from test import Case, Test
    cases = Case()
    cases.add_cases((
        (5, 2),
        (10, 4)
    ))
    Test(cases, Solution(), 'countTriples').run()