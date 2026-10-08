class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        path = []

        def dfs(i: int, left: int) -> None:
            if left == 0:
                # 找到一个合法组合
                ans.append(path.copy())
                return

            if i == len(candidates) or left < 0:
                return

            # 不选
            dfs(i + 1, left)

            # 选
            path.append(candidates[i])
            dfs(i, left - candidates[i])
            path.pop()  # 恢复现场

        dfs(0, target)
        return ans

if __name__ == "__main__":
    obj = Solution()
    print(obj.combinationSum([2,3,6,7], 7))