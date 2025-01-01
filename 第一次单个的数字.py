s = str(input())
b = 0
from collections import Counter
s1 = Counter(s)
for i in s:
    if s1[i] == 1:
        print(i)
        break
    if s1[i] != 1:
        b += 1
if b == len(s):
    print('no')