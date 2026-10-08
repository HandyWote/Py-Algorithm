a = int(input())
b = input().split()
b = [int(x) for x in b]
i = 0
c = []
d = []
for j in b:
    c = []
    for k in b[:i+1]:
        if j > k:
            c.append(1)
    d.append(sum(c))
    i += 1
d = [str(f) for f in d]
d = ' '.join(d)
print(d)