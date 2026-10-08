n = int(input())
count = 1
for i in range(1,n+1):
    a = []
    for j in range(1,n+1):
        a.append(str("%02d" % count))
        count += 1
    print("".join(a))
count = 1
print()
for i in range (1,n+1):
    a = []
    for j in range (i):
        a.append(str("%02d" % count))
        count += 1
    max_width = 2 * n
    print("".join(a).rjust(max_width))