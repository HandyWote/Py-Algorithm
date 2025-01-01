n,m = map(int,input().split())
a = [int(input()) for _ in range(n)]
ans = []
if n == 1 or n == m:
    print(sum(a))    
else:
    for i in range(n):
        if i+m+1 < n:
            ans.append(sum(a[i:i+m]))
    print(min(ans))