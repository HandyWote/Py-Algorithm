a,b = map(int,input().split())
if b < 0:
    print(-1*abs(a))
if b > 0:
    print(abs(a))