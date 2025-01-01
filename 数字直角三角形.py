n = int(input())
b = 1
while n >= 1:
    a = []
    for i in range(n):
        a.append("{:02d}".format(b))
        b += 1
    print(''.join(a))
    n -= 1