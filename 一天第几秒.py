a = input().split()
h,m,s = map(int,a[0:3])
d = str(a[3])
if d == "A":
    h += 0
elif d == 'P':
    h += 12
m = m + h*60
s = s + m*60
print(s)