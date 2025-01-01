n = int(input())
if n < 0:
    sn = str(n)[1:]
    rn = int(sn[::-1])
    print(-rn)
else:
    print(int(str(n)[::-1]))