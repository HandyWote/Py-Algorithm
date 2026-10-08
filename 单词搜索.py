class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        visited = set()
        m, n = len(board), len(board[0])
        def dfs(i: int, j: int) -> bool:
            if not(0 <= i < m and 0 <= j < n) or (i, j) in visited or board[i][j] != word[len(visited)]:
                return False
            visited.add((i, j))
            dfs_result = len(visited) == len(word) or dfs(i+1, j) or dfs(i-1, j) or dfs(i, j+1) or dfs(i, j-1)
            if not dfs_result:
                visited.remove((i, j))
            return dfs_result
            
        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if ch == word[0] and dfs(i, j):
                    return True
        return False

if __name__ == '__main__':
    cases = {
        'input':[
            ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"),
            ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"),
            ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
        ],
        'output':[
            True,
            True,
            False
        ]
    }
    from test import Test
    Test(cases, Solution(), 'exist').run()