n = int(input())
a = input().split()
a = [int(i) for i in a]
b = []
c = []

a.sort()
m = sum(a[-3::])
set_a = set(a)

for i in range(len(a)):
    for j in range(i+1, len(a)):
        b.append(a[i] + a[j])

set_b = set(b)
for i in range(len(a)):
    for j in range(i+1, len(a)):
        for k in range(j+1, len(a)):
            c.append(a[i] + a[j] + a[k])

set_c = set(c)

ans = [x for x in set(set_a|set_b|set_c) if x <= m]
print(len(ans) + 1)