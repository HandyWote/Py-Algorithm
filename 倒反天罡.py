def rotate_matrix(matrix):
    # 获取矩阵的行数和列数
    rows = len(matrix)
    cols = len(matrix[0])
    return [[matrix[rows - 1 - r][c] for r in range(rows)] for c in range(cols)]
# 读取矩阵的维度和旋转角度
a, n = map(int, input().split())
matrix = [input().split() for _ in range(a)]

# 旋转矩阵
rotated_matrix = rotate_matrix(matrix)

# 打印旋转后的矩阵
for row in rotated_matrix:
    print(' '.join(row))