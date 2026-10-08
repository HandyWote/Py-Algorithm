def get_input():
    n, m = map(int, input().split())
    grid = list()
    single_sum = 0
    for _ in range(n):
        temp = [int(i) for i in input()]
        single_sum += sum(temp)
        grid.append(temp)
    return n, m, grid, single_sum

def pre_sum(n, m, grid):
    right = [[0] * m for _ in range(n)]
    down = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m-1, -1, -1):
            if grid[i][j]:
                right[i][j] = 1 + (right[i][j+1] if j+1 < m else 0)
    
    for i in range(n-1, -1, -1):
        for j in range(m):
            if grid[i][j]:
                down[i][j] = 1 + (down[i+1][j] if i+1 < n else 0)
    return right, down

def get_total(n, m, right, down, sigel_sum): 
    """刻痕总数"""
    horizontal = sum(right[i][j] for i in range(n) for j in range(m) if right[i][j])
    vertical = sum(down[i][j] for i in range(n) for j in range(m) if down[i][j])
    total = horizontal + vertical - sigel_sum
    return total * (total-1)

def get_through(n, m, right, down):
    """算经过每个格子的水平(>=2)/垂直(>=2)刻痕数"""
    h_through = [[0]*m for _ in range(n)]
    v_through = [[0]*m for _ in range(n)]
    for i in range(n):
        diff = [0]*(m+1)
        for j in range(m):
            if right[i][j] >= 2:
                diff[j] += 1
                diff[j + right[i][j]] -= 1
        s = 0
        for j in range(m):
            s += diff[j]
            h_through[i][j] = s
    for j in range(m):
        diff = [0]*(n+1)
        for i in range(n):
            if down[i][j] >= 2:
                diff[i] += 1
                diff[i + down[i][j]] -= 1
        s = 0
        for i in range(n):
            s += diff[i]
            v_through[i][j] = s
    return h_through, v_through


def get_hv_intersect(n, m, h_through, v_through):
    """水平(>=2)与垂直(>=2)相交"""
    return 2 * sum(h_through[i][j] * v_through[i][j] for i in range(n) for j in range(m))


def get_hh_intersect(n, m, right):
    """同行两条水平(>=2)刻痕相交（含自身交叉）"""
    total = 0
    for i in range(n):
        # 计算该行经过每个位置的水平(>=2)刻痕数
        through = [0]*m
        diff = [0]*(m+1)
        for j in range(m):
            if right[i][j] >= 2:
                diff[j] += 1
                diff[j + right[i][j]] -= 1
        s = 0
        for j in range(m):
            s += diff[j]
            through[j] = s
        # 每个位置，经过它的刻痕中任选两条（有序）
        for j in range(m):
            total += through[j] * (through[j] - 1)
    return total


def get_vv_intersect(n, m, down):
    """同列两条垂直(>=2)刻痕相交（含自身交叉）"""
    total = 0
    for j in range(m):
        through = [0]*n
        diff = [0]*(n+1)
        for i in range(n):
            if down[i][j] >= 2:
                diff[i] += 1
                diff[i + down[i][j]] -= 1
        s = 0
        for i in range(n):
            s += diff[i]
            through[i] = s
        for i in range(n):
            total += through[i] * (through[i] - 1)
    return total


def solve():
    n, m, grid, single_sum = get_input()
    right, down = pre_sum(n, m, grid)

    total_pairs = get_total(n, m, right, down, single_sum)
    h_through, v_through = get_through(n, m, right, down)

    intersect = (get_hv_intersect(n, m, h_through, v_through)
                 + get_hh_intersect(n, m, right)
                 + get_vv_intersect(n, m, down))

    # 单点-单点相交：每个位置只有1条单点刻痕，不可能自交 = 0
    # 单点-水平(>=2)相交（单点在水平线段上）
    sh = sum(h_through[i][j] for i in range(n) for j in range(m) if grid[i][j])
    intersect += 2 * sh
    # 单点-垂直(>=2)相交（单点在垂直线段上）
    sv = sum(v_through[i][j] for i in range(n) for j in range(m) if grid[i][j])
    intersect += 2 * sv

    print(total_pairs - intersect)


if __name__ == '__main__':
    solve()