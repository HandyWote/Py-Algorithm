n = int(input())
lantern = [0] * 2000001
for i in range(n):
    a = input().split()
    t = int(a[1])
    for j in range(1,t+1):
        lantern[int(float(a[0])*j)] += 1
for index, value in enumerate(lantern):
    if value % 2 != 0:
        print(index)