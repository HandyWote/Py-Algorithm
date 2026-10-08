class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = list()

        def backtrack(start, path, current):
            nonlocal res
            if target == current:
                res.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if current + candidates[i] > target:
                    break

                path.append(candidates[i])
                backtrack(i + 1, path, current + candidates[i])
                path.pop()
                
        backtrack(0, [], 0)
        return res

# class Solution:
#     def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        
#         def dfs(start, left):
#             if left == 0:
#                 res.append(path[:])
#                 return
#             if left < 0:
#                 return
#             if start >= n:
#                 return
#             for i in range(start, n):
#                 if i > start and candidates[i] == candidates[i - 1]:
#                     continue
#                 path.append(candidates[i])
#                 dfs(i + 1, left - candidates[i])
#                 path.pop()
        
#         candidates.sort()
#         n = len(candidates)
#         res = list()
#         path = list()
#         dfs(0, target)
#         return res

if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum2([10,1,2,7,6,1,5], 8))  # Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
    print(s.combinationSum2([2,5,2,1,2], 5))  # Output: [[1,2,2],[5]]