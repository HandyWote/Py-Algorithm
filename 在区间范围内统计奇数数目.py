class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2

if __name__ == "__main__":
    from test import Test, Case
    cases = Case.add_cases(
        (((3, 7), 3),
        ((8, 10), 1),)
    )
    Test(cases, Solution(), "countOdds").run()