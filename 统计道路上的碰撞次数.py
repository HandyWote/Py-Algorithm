class Solution:
    def countCollisions(self, directions: str) -> int:
        directions = directions.lstrip('L')
        directions = directions.rstrip('R')
        return len(directions) - directions.count('S')


if __name__ == "__main__":
    cases = {
        'input': [
            "RLRSLL",
            "LLRR",
            "SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR"
        ],
        'output': [
            5,
            0,
            20
        ]
    }
    from test import Test
    Test(cases, Solution(), 'countCollisions').run()