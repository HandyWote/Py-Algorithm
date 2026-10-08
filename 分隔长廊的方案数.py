class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 1_000_000_007
        ans = 1
        cnt_s = last_s = 0

        for i, c in enumerate(corridor):
            if c == 'S':
                cnt_s += 1
                if cnt_s > 2 and cnt_s % 2:
                    ans = (ans * (i - last_s)) % MOD
                last_s = i
 
        if cnt_s == 0 or cnt_s % 2:
            return 0
        return ans


if __name__ == "__main__":
    from test import Test, Case
    cases = Case(
        [
            ("SSPPSPS", 3),
            ("PPSPSP", 1),
            ("S", 0)
        ]
    )
    Test(cases, Solution(), "numberOfWays").run()