a = [int(x) for x in input().split()]
h = int(input()) + 30
ans = 0
for i in a:
    if i <= h:
        ans += 1
print(ans)