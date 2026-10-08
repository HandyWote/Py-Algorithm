n = int(input())
for _ in range (n):
    l = input().split()
    l[1] = int(l[1]) + 1
    if int(l[2])*1.2 >= 600:
        l[2] = int(600)
    elif int(l[2])*1.2 < 600:
        l[2] = int(int(l[2])*1.2)
    print(' '.join(map(str,l)))