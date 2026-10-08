class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        x = 0
        for op in operations:
            if op[1] == '+':
                x += 1
            else:
                x -= 1
        return x

def test():
    cases = {
        'input': [
            ["--X","X++","X++"],
            ["++X","++X","X++"],
            ["X++","++X","--X","X--"]
        ],
        'expected': [
            1,
            3,
            0
        ]
    }
    for i, e in zip(cases['input'], cases['expected']):
        assert Solution().finalValueAfterOperations(i) == e
        print(f'case {i} pass')
    
if __name__ == "__main__":
    test()