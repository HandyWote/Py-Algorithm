class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        def backtrack(start, path):
            if len(path) == k:
                result.append(path[:])
                return
            
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(1, [])
        return result

def test():
    cases = {
        'input':[
            (4, 2),
            (1, 1)
        ],
        'output': [
            [[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]],
            [[1]]
        ]
    }
    s = Solution()
    for i, c in enumerate(cases['input']):
        assert s.combine(c[0], c[1]).sort() == cases['output'][i].sort(), f"Test {i+1} faild, expected {cases['output'][i]} but get {s.combine(c[0], c[1])}"
        print(f"Test {i+1} passed")
    print('All test passed')

if __name__ == "__main__":
    test()