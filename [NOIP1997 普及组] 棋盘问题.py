def count_squares_and_rectangles(n, m):
    ans1 = 0  # 正方形的数量
    ans2 = 0  # 长方形的数量
    for i in range(n):
        for j in range(m):
            for ii in range(i + 1, n + 1):
                for jj in range(j + 1, m + 1):
                    if ii - i == jj - j:
                        ans1 += 1
                    else:
                        ans2 += 1
    return ans1, ans2

n, m = map(int, input().split())
ans1, ans2 = count_squares_and_rectangles(n, m)
print(ans1,ans2)