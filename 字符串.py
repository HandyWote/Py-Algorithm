s = input()
t = input()
from collections import Counter
c1 = Counter(s)
c2 = Counter(t)
ans = 0
for i in range(26):
    t = chr(ord('a') + i)
    ans += min(c1[t],c2[t])
print(ans)