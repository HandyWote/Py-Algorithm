w, x, h = map(int, input().split())
v = [[[True] * w for _ in range(x)]for _ in range(h)]

t = int(input())
for i in range(t):
    x1,y1,z1,x2,y2,z2 = map(int, input().split())
    for j in range(x1-1,x2):
        for k in range(y1-1,y2):
            for l in range(z1-1,z2):
                if v[j][k][l]:
                    v[j][k][l] = False

ans = 0
for i in v:
    for j in i:
        for k in j:
            if k:
                ans += 1

print(ans)