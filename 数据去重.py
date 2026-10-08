n=int(input())
f=input().split()
f=[int(x) for x in f]
q=[]
for i in range(n):
    if q.count(f[i])==0:
        print(f[i],end=' ')
        q.append(f[i])
