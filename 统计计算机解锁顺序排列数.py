class Solution:
    def countPermutations(self, complexity: list[int]) -> int:
        MOD = 1_000_000_007
        ans = 1
        for i in range(1, len(complexity)):
            if complexity[i] <= complexity[0]:
                return 0
            ans = ans * i % MOD
        return ans



if __name__ == "__main__":
    from test import Test, Case
    cases = Case()
    cases.add_cases(
        (
            ([1,2,3], 2),
            ([3,3,3,4,4,4], 0),
            ([3470,9997,31628,55082,43915,14129,49183,99427,71495,31577,74287,96625,55548,56522,45502,20407,24812,48500,48200,57692,20660,50351,29619,88947,65929,3471,37527,17931,62499,69198,45737,38605,94241,68261,61653,97116,97217,79694,58943,54248,24192,39712,34398,84847,89541,90309,17607,67739,84663,35600], 726372166)
        )
    )
    Test(cases, Solution(), 'countPermutations').run()