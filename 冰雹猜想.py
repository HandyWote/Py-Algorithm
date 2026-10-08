a = int(input())
l = []
l.append(a)
while a != 1:
    if a % 2 == 0:
        a = int(a/2)
        l.append(a)
    else:
        a = int(3*a+1)
        l.append(a)
l.reverse()
l = [str(x) for x in l]
l = " ".join(l)
print(l)