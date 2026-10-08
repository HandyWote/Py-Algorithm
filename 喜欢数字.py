n = int(input())
a = []
#小A
if n%2 == 0 and 12>=n>=4:
    a.append(1)
else:
    a.append(0)
#Uim
if n%2 == 0 or 12>=n>=4 or (n%2 == 0 and 12>=n>=4):
    a.append(1)
else:
    a.append(0)
#小B
if  (not n%2 == 0 and 12>=n>=4) or (n%2 == 0 and not 12>=n>=4):
    a.append(1)
else:
    a.append(0)
#正妹
if not n%2 == 0 and not 12>=n>=4:
    a.append(1)
else:
    a.append(0)
print(*a)