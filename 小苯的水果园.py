from collections import Counter
for _ in range (int(input())):
    ln,lq = map(int,input().split())
    n = list(input().split())
    n1 = Counter(n)
    n2 = list(n1.items())
    q = list(map(int,input().split()))
    for i in range(1,q[-1]+1):
        for j,k in n2:
            if k == i:
                n1.pop(j)
        if i == q[0]:
            print(sum(n1.values()),end=' ')
            q.pop(0)