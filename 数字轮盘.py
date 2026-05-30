t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    k=k%n
    if k==0:
        ans=0
        print(ans)
        continue
    if n%2==0 and k%2!=0:
        ans=-1
    elif n%2==0 and k%2==0:
        ans=(n-k)//2
    elif n%2!=0 and k%2!=0:
        ans=(n-k)//2
    else:
        ans=(n-k-1)//2+1+(n-1)//2
    print(ans)