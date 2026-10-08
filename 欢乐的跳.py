a = input().split()
n = int(a[0])
b = list(map(int,a[1::]))
c = []
d = [i for i in range(1,n)]
for i in range(n-1):
    c.append(abs(b[i]-b[i+1]))
c.sort()
if d == c:
    print("Jolly")
else:
    print("Not jolly")