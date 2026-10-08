n = int(input())
ans = 0
for _ in range(n):
    imformation = input().split()
    if float(imformation[1]) >= 37.5 and int(imformation[2]) == 1:
        ans += 1
        print(imformation[0])
print(ans)