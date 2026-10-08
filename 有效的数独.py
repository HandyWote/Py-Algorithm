class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        r_h = [[False] * 9 for _ in range(9)]
        c_h = [[False] * 9 for _ in range(9)]
        s_h = [[[False] * 9 for _ in range(3)] for _ in range(3)]

        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num == '.': continue
                num = int(num)
                if r_h[i][num-1] or c_h[j][num-1] or s_h[i//3][j//3][num-1]:
                    return False
                r_h[i][num-1], c_h[j][num-1], s_h[i//3][j//3][num-1] = True, True, True
        return True

if __name__ == "__main__":
    obj = Solution()
    print(obj.isValidSudoku([["5","3",".",".","7",".",".",".","."],
                             ["6",".",".","1","9","5",".",".","."],
                             [".","9","8",".",".",".",".","6","."],
                             ["8",".",".",".","6",".",".",".","3"],
                             ["4",".",".","8",".","3",".",".","1"],
                             ["7",".",".",".","2",".",".",".","6"],
                             [".","6",".",".",".",".","2","8","."],
                             [".",".",".","4","1","9",".",".","5"],
                             [".",".",".",".","8",".",".","7","9"]]))