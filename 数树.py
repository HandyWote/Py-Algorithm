a,b = map(int,input().split())
alm = []
for i in range (b):
    x,y = map(int,input().split())
    metro = [int(q) for q in range(x,y+1)]
    alm += metro
alm = set(alm)
road = a - len(alm)
print(road+1)