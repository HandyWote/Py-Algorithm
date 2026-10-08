class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        m, n = len(matrix), len(matrix[0])
        zero_rows = set()
        zero_cols = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        for i in zero_rows:
            for j in range(n):
                matrix[i][j] = 0
        for j in zero_cols:
            for i in range(m):
                matrix[i][j] = 0