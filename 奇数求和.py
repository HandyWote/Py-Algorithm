a,b = map(int,input().split())
l = []
for i in range (a,b+1):
    if (i)%2==0:
        continue
    else:
        l.append(i)
print(sum(l))