n = int(input())
a = [[0 for i in range(n+1)] for j in range(n+1)]
a[0][0] = 1
for y in range(1,n+1):
    for x in range(n+1):
        a[y][x] = a[y-1][x-1] + a[y-1][x]
for i in range(n):
    for j in range(n):
        if (a[i][j] != 0):
            print(a[i][j],end=' ')
    print('')