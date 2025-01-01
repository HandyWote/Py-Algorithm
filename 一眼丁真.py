n = int(input())
yydz = []
for i in range(n):
    a = input().split()
    if a[0][0] == 'y' and a[1][0] == 'y' and a[2] == 'ding' and a[3] =='zhen':
        yydz.append('Yes')
    else:
        yydz.append('No')
for i in yydz:
    print(i)