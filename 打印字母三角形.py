a = int(input())
c = 1
b = 0
for k in range (a):
    s=''
    for i in range(c):
        if b+65 >= 91:
            b = 0
        s += chr(65+b)
        b += 1
    print(s)
    c += 1