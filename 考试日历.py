date = int(input())
day = int(input())
d = day % 7
a = date + d
if a > 7:
    a = a - 7
print(a)