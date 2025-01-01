n,k = map(int,input().split())
a = []
b = []
for i in range(1,n+1):
    if i % k == 0:
        a.append(i)
    else:
        b.append(i)
print("%.1f %.1f"%(sum(a)/len(a),sum(b)/len(b)))