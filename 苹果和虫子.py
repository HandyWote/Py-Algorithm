m,t,s = map(int,input().split())
if t == 0 or s/t > m:
    print(0)
else:
    print(int(m-s/t))