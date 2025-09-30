class Solution:
    def jump(self, nums: list[int]) -> int:

        def dfs(i: int) -> int:
            if i >= len(nums) - 1:
                return 0
            if i in memo:
                return memo[i]
            min_jumps = float('inf')
            for j in range(1, nums[i] + 1):
                min_jumps = min(min_jumps, 1 + dfs(i + j))
            memo[i] = min_jumps
            return min_jumps
        memo = {}        
        return dfs(0)

if __name__ == "__main__":
    s = Solution()
    print(s.jump([2,3,1,1,4]))  # 应该输出2
    print(s.jump([2,3,0,1,4]))  # 应该输出2
