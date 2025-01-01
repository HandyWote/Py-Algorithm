n = int(input())
a = list(map(int, input().split()))
a.sort()
day = 0
index = 0

for i in range(1, n + 1):
    if index < len(a):
        while index < len(a) and a[index] < i:
            index += 1
        if index < len(a) and a[index] >= i:
            day += 1
            index += 1
        else:
            break
    else:
        break

print(day)