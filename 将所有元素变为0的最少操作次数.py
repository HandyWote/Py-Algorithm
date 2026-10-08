class Solution:
    def minOperations(self, nums: list[int]) -> int:
        """
        将所有元素变为0的最少操作次数
        使用单调栈的方法解决
        """
        ans = 0
        st = []
        for x in nums:
            # 当栈不为空且当前元素小于栈顶元素时，需要操作
            while st and x < st[-1]:
                st.pop()
                ans += 1
            # 如果 x 与栈顶相同，那么 x 与栈顶可以在同一次操作中都变成 0，x 无需入栈
            if not st or x != st[-1]:
                st.append(x)
        return ans + len(st) - (st[0] == 0)  # 0 不需要操作

def test():
    cases = {
        'input':[
            [0,2],
            [3,1,2,1],
            [1,2,1,2,1,2],
            [7,2,0,4,2]
        ],
        'output': [
            1,
            3,
            4,
            4
        ]
    }
    s = Solution()
    for i, c in enumerate(cases['input']):
        print(f"\n=== Test {i+1}: {c} ===")
        result = s.minOperations(c)
        expected = cases['output'][i]
        print(f"Result: {result}, Expected: {expected}")
        assert result == expected, f"Test {i+1} failed, expected {expected} but get {result}"
        print(f"Test {i+1} passed")    
    print('All test passed')

if __name__ == "__main__":
    test()