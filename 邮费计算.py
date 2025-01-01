a = input().split()
b = int(a[0])
c = str(a[1])
m = 0
if b <= 1000:
    m = 8
if b > 1000:
    e = (b-1000) % 500
    k = (b-1000)/500
    if e == 0:
        m = 8 + k*4
    if e != 0:
        m = 8 + (int(k)+1)*4 

if c == 'y':
    m = m + 5
elif c == "n":
    m = m
print(int(m))