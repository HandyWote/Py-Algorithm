from collections import Counter
a = list(map(int,input().split()))
a.sort()
b = []
for i in range(1,a[2]+1):
    for j in range(1,a[1]+1):
        for k in range(1,a[0]+1):
            b.append(i+j+k)
bc = Counter(b)
print(bc.most_common(1)[0][0])