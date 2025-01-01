n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
for i in a:
    for j in b:
        if i == j:
            b.remove(j)
            break
print(m-len(b))