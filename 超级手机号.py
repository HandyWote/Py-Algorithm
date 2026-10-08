n = int(input())
ans = 0
for i in range(n):
    phone = [int(x) for x in input()]
    if len(set(phone)) == 1:
        ans += 1
print(ans)