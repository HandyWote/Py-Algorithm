a = int(input())
b = input().split()
b = [int(x) for x in b]
c = []
ans = 0
for i in range(a):
    c.append(b[i])
    for j in range(i+1,a):
        c.append(b[j])
        if pow(sum(c),0.5) == int(pow(sum(c),0.5)):
            ans+=1
        c.remove(b[j])
    c = []
print(ans)