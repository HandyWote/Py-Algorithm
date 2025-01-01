a = list(map(int,input().split()))
count = a[0]
u = 1
for i in a[1:]:
    for j in range(i):
        if count == 0:
            print('')
            count = a[0]
        if u == 1:
            print(0,end='')
            count -= 1
        elif u == -1:
            print(1,end='')
            count -= 1
    u *= -1