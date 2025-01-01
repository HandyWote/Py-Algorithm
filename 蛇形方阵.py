n = int(input())
grids = [[0] * n for _ in range(n)]
y, l, r, b = 0, 0, n - 1,  n - 1
num = 1
while True:
    for x in range(l, r + 1): # 从左到右
        grids[y][x] = num
        num += 1
    y += 1
    if y > b: break

    for x in range(y, b + 1): # 从上到下
        grids[x][r] = num
        num += 1
    r -= 1
    if r < l: break

    for x in range(r, l - 1, -1): # 从右到左
        grids[b][x] = num
        num += 1
    b -= 1
    if  b < y: break
    
    for i in range(b, y - 1, -1): # 从下到上
        grids[i][l] = num
        num += 1
    l += 1
    if r < l: break
 
for i in range(n):
    for x in range(n):
        if grids[i][x] < 10:
            grids[i][x] = " "+str(grids[i][x])
    print(' '+' '.join(str(x) for x in grids[i]))