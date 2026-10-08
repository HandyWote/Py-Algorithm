class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m, n = len(matrix) if matrix else 0, len(matrix[0]) if matrix else 0
        if m == 0 or n == 0:
            return []
        result = []
        left, right, top, bottom = 0, n - 1, 0, m - 1
        while left <= right and top <= bottom:
            # Traverse from left to right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            
            # Traverse from top to bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:
                # Traverse from right to left
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            
            if left <= right:
                # Traverse from bottom to top
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        return result
    
if __name__ == "__main__":
    s = Solution()
    print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
    print(s.spiralOrder([[1, 2], [3, 4]]))                  # Output: [1, 2, 4, 3]
    print(s.spiralOrder([[1]]))                             # Output: [1]
    print(s.spiralOrder([]))                                # Output: []