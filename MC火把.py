n,m,k = map(int,input().split())
vis = [[False] * n for i in range(n)]
dic = [(-1,-1),(1,1),(1,-1),(-1,1)]
for _ in range(m):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    for c in dic:
        dx,dy = x+c[0],y+c[1]
        if 0 <= dx < n and 0 <= dy < n:
            vis[dx][dy] = True
    for i in range(max(x-2,0),min(x+3,n)):
        vis[i][y] = True
    for j in range(max(y-2,0),min(y+3,n)):
        vis[x][j] = True
for _ in range(k):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    for i in range(max(x-2,0),min(x+3,n)):
        for j in range(max(y-2,0),min(y+3,n)):
            vis[i][j] = True
ans = 0
for i in range(n):
    for j in range(n):
        if not vis[i][j]:
            ans += 1
print(ans) 