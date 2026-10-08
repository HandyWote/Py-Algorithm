n = int(input())
p = list(map(int,input().split()))
ans = [0,0,0,0,0,0,0]
for i in range (n):
    b = list(map(int,input().split()))
    b1 = set(b + p)
    l = 14 - len(b1)
    if l == 1:
        ans[-1] += 1
    elif l == 2:
        ans[-2] += 1
    elif l == 3:
        ans[-3] += 1
    elif l == 4:
        ans[-4] += 1
    elif l ==5:
        ans[-5] += 1
    elif l ==6:
        ans[-6] += 1
    elif l ==7:
        ans[-7] += 1
print(' '.join([str(i) for i in ans]))