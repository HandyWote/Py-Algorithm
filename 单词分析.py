from collections import Counter 

s = input()
cs = Counter(s)
c = cs.most_common(1)
cl = len(c)
for i in range(cl):
    print(c[i][0])
    print(c[i][1])