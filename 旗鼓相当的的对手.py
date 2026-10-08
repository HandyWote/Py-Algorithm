a = int(input())
g = []
for i in range(a):
    g.append([int(i) for i in input().split()])
ans = 0
for i in range(a):
    for j in range(i+1,a):
        if abs(g[i][0]-g[j][0])<=5 and abs(g[i][1]-g[j][1])<=5 and abs(g[i][2]-g[j][2])<=5 and abs(sum(g[i])-sum(g[j]))<=10:
            ans += 1
print(ans)