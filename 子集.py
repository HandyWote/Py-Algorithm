class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        
        def backtrack(start, path):
            ans.append(path[:])
            remaining_elements = len(nums) - start
            for i in range(start, len(nums)):
                if remaining_elements == 0 and len(path) > 0:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
                remaining_elements -= 1
        backtrack(0, [])
        return ans
    
def test():
    cases = {
        'input':[
            [1,2,3],
            [0]
        ],
        'output': [
            [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]],
            [[],[0]]
        ]
    }
    s = Solution()
    for i, c in enumerate(cases['input']):
        result = s.subsets(c)
        expected = cases['output'][i]
        assert sorted(result) == sorted(expected), f"Test {i+1} failed, expected {expected} but get {result}"
        print(f"Test {i+1} passed")    
    print('All test passed')

if __name__ == "__main__":
    test()